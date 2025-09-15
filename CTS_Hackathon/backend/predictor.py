#!/usr/bin/env python3
"""
Predictor module for hospital readmission prediction.
Handles model loading, preprocessing, and inference.
"""

import joblib
import pandas as pd
import numpy as np
import logging
from typing import Dict, List, Tuple
import os

logger = logging.getLogger(__name__)

class ReadmissionPredictor:
    """Hospital readmission prediction class."""
    
    def __init__(self, model_path=None):
        """Initialize the predictor with model loading."""
        if model_path is None:
            # Get the directory of this script
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up one level to the project root, then to models
            project_root = os.path.dirname(current_dir)
            model_path = os.path.join(project_root, 'models', 'readmit_pipeline.joblib')
        
        self.model_path = model_path
        self.model = None
        self.feature_names = None
        self.feature_importance = None
        self.load_model()
    
    def load_model(self):
        """Load the trained model pipeline and related files."""
        try:
            # Get the models directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(current_dir)
            models_dir = os.path.join(project_root, 'models')
            
            # Load the main pipeline
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
                logger.info(f"Model loaded successfully from {self.model_path}")
            else:
                logger.error(f"Model file not found: {self.model_path}")
                return
            
            # Load feature names
            feature_names_path = os.path.join(models_dir, 'feature_names.joblib')
            if os.path.exists(feature_names_path):
                self.feature_names = joblib.load(feature_names_path)
                logger.info("Feature names loaded successfully")
            
            # Load feature importance
            importance_path = os.path.join(models_dir, 'feature_importance.joblib')
            if os.path.exists(importance_path):
                self.feature_importance = joblib.load(importance_path)
                logger.info("Feature importance loaded successfully")
                
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            self.model = None
    
    def preprocess_input(self, patient_data: Dict) -> pd.DataFrame:
        """Preprocess patient data for prediction."""
        try:
            # Create age mapping
            age_mapping = {
                '[40-50)': 0, '[50-60)': 1, '[60-70)': 2, 
                '[70-80)': 3, '[80-90)': 4, '[90-100)': 5
            }
            
            # Binary mappings
            binary_mappings = {
                'glucose_test': {'no': 0, 'normal': 1, 'high': 2},
                'A1Ctest': {'no': 0, 'normal': 1, 'high': 2},
                'change': {'no': 0, 'yes': 1},
                'diabetes_med': {'no': 0, 'yes': 1}
            }
            
            # Start with numeric features
            processed_data = {
                'age_numeric': age_mapping.get(patient_data.get('age', '[70-80)'), 3),
                'time_in_hospital': patient_data.get('time_in_hospital', 0),
                'n_lab_procedures': patient_data.get('n_lab_procedures', 0),
                'n_procedures': patient_data.get('n_procedures', 0),
                'n_medications': patient_data.get('n_medications', 0),
                'n_outpatient': patient_data.get('n_outpatient', 0),
                'n_inpatient': patient_data.get('n_inpatient', 0),
                'n_emergency': patient_data.get('n_emergency', 0)
            }
            
            # Add binary encoded features
            for feature, mapping in binary_mappings.items():
                value = patient_data.get(feature, 'no')
                processed_data[f'{feature}_encoded'] = mapping.get(value, 0)
            
            # Handle categorical features with one-hot encoding
            categorical_features = ['medical_specialty', 'diag_1', 'diag_2', 'diag_3']
            
            # Get all possible categorical values from feature names if available
            if self.feature_names:
                for cat_feature in categorical_features:
                    # Find all columns that start with this categorical feature
                    cat_columns = [col for col in self.feature_names if col.startswith(f'{cat_feature}_')]
                    
                    # Initialize all to 0
                    for col in cat_columns:
                        processed_data[col] = 0
                    
                    # Set the appropriate column to 1
                    value = patient_data.get(cat_feature, 'Missing')
                    target_col = f'{cat_feature}_{value}'
                    if target_col in processed_data:
                        processed_data[target_col] = 1
            
            # Create DataFrame with all expected features
            if self.feature_names:
                # Initialize with zeros for all expected features
                df_data = {col: 0 for col in self.feature_names}
                # Update with our processed data
                df_data.update(processed_data)
                df = pd.DataFrame([df_data])
            else:
                df = pd.DataFrame([processed_data])
            
            return df
            
        except Exception as e:
            logger.error(f"Error preprocessing input: {str(e)}")
            raise
    
    def predict(self, patient_data: Dict) -> Dict:
        """Make prediction for a patient."""
        if self.model is None:
            raise ValueError("Model not loaded")
        
        try:
            # Preprocess input
            input_df = self.preprocess_input(patient_data)
            
            # Make prediction
            prediction_proba = self.model.predict_proba(input_df)[0]
            prediction = self.model.predict(input_df)[0]
            
            # Get probability for readmission (class 1)
            readmit_probability = prediction_proba[1] if len(prediction_proba) > 1 else prediction_proba[0]
            
            # Determine prediction text
            will_readmit = prediction == 1
            prediction_text = "WILL readmit" if will_readmit else "WILL NOT readmit"
            
            # Get top risk factors
            risk_factors = self.get_risk_factors(input_df, readmit_probability)
            
            result = {
                'readmit_probability': float(readmit_probability),
                'readmit_probability_percent': f"{readmit_probability * 100:.1f}%",
                'prediction': prediction_text,
                'will_readmit': bool(will_readmit),
                'risk_factors': risk_factors,
                'patient_data': patient_data
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error making prediction: {str(e)}")
            raise
    
    def get_risk_factors(self, input_df: pd.DataFrame, probability: float) -> List[Dict]:
        """Calculate top 3 risk factors using feature importance."""
        try:
            risk_factors = []
            
            if self.feature_importance is None:
                # Fallback to simple heuristic
                return self.get_heuristic_risk_factors(input_df, probability)
            
            # Calculate feature contributions
            feature_contributions = []
            
            for feature in input_df.columns:
                if feature in self.feature_importance:
                    importance = self.feature_importance[feature]
                    value = input_df[feature].iloc[0]
                    contribution = importance * abs(value) if value != 0 else 0
                    
                    feature_contributions.append({
                        'feature': feature,
                        'importance': importance,
                        'value': value,
                        'contribution': contribution
                    })
            
            # Sort by contribution and get top 3
            feature_contributions.sort(key=lambda x: x['contribution'], reverse=True)
            top_features = feature_contributions[:3]
            
            for i, feature_info in enumerate(top_features, 1):
                feature_name = self.format_feature_name(feature_info['feature'])
                contribution_score = feature_info['contribution']
                
                risk_factors.append({
                    'rank': i,
                    'factor': feature_name,
                    'contribution': f"{contribution_score:.3f}",
                    'impact': "High" if contribution_score > 0.1 else "Medium" if contribution_score > 0.05 else "Low"
                })
            
            return risk_factors
            
        except Exception as e:
            logger.error(f"Error calculating risk factors: {str(e)}")
            return self.get_heuristic_risk_factors(input_df, probability)
    
    def get_heuristic_risk_factors(self, input_df: pd.DataFrame, probability: float) -> List[Dict]:
        """Fallback heuristic for risk factors when feature importance is not available."""
        risk_factors = []
        
        # Simple heuristic based on common medical knowledge
        heuristic_factors = [
            ('time_in_hospital', 'Length of hospital stay'),
            ('n_medications', 'Number of medications'),
            ('age_numeric', 'Patient age'),
            ('n_lab_procedures', 'Number of lab procedures'),
            ('diabetes_med_encoded', 'Diabetes medication'),
            ('n_inpatient', 'Previous inpatient visits'),
            ('change_encoded', 'Medication changes')
        ]
        
        factor_scores = []
        for feature, display_name in heuristic_factors:
            if feature in input_df.columns:
                value = input_df[feature].iloc[0]
                # Simple scoring based on value magnitude
                score = abs(value) * 0.1 if value != 0 else 0
                factor_scores.append((display_name, score))
        
        # Sort and get top 3
        factor_scores.sort(key=lambda x: x[1], reverse=True)
        
        for i, (factor_name, score) in enumerate(factor_scores[:3], 1):
            risk_factors.append({
                'rank': i,
                'factor': factor_name,
                'contribution': f"{score:.3f}",
                'impact': "High" if score > 0.5 else "Medium" if score > 0.2 else "Low"
            })
        
        return risk_factors
    
    def format_feature_name(self, feature: str) -> str:
        """Format feature names for display."""
        # Mapping of technical names to readable names
        name_mapping = {
            'age_numeric': 'Patient Age',
            'time_in_hospital': 'Length of Hospital Stay',
            'n_lab_procedures': 'Number of Lab Procedures',
            'n_procedures': 'Number of Procedures',
            'n_medications': 'Number of Medications',
            'n_outpatient': 'Outpatient Visits',
            'n_inpatient': 'Previous Inpatient Visits',
            'n_emergency': 'Emergency Visits',
            'glucose_test_encoded': 'Glucose Test Result',
            'A1Ctest_encoded': 'A1C Test Result',
            'change_encoded': 'Medication Changes',
            'diabetes_med_encoded': 'Diabetes Medication'
        }
        
        # Handle one-hot encoded features
        if '_' in feature and feature not in name_mapping:
            parts = feature.split('_', 1)
            if len(parts) == 2:
                prefix, value = parts
                prefix_mapping = {
                    'medical_specialty': 'Medical Specialty',
                    'diag_1': 'Primary Diagnosis',
                    'diag_2': 'Secondary Diagnosis',
                    'diag_3': 'Additional Diagnosis'
                }
                if prefix in prefix_mapping:
                    return f"{prefix_mapping[prefix]}: {value}"
        
        return name_mapping.get(feature, feature.replace('_', ' ').title())
