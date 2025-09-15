#!/usr/bin/env python3
"""
Train and save a hospital readmission prediction model pipeline.
This script creates a complete preprocessing and prediction pipeline.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.impute import SimpleImputer
import joblib
import os
from datetime import datetime

def create_model_pipeline():
    """Create and train the hospital readmission prediction pipeline."""
    
    # Load the dataset
    print("Loading dataset...")
    df = pd.read_csv('data/hospital_readmissions.csv')
    
    # Data preprocessing
    print("Preprocessing data...")
    
    # Create age groups mapping
    age_mapping = {
        '[40-50)': 0, '[50-60)': 1, '[60-70)': 2, 
        '[70-80)': 3, '[80-90)': 4, '[90-100)': 5
    }
    df['age_numeric'] = df['age'].map(age_mapping)
    
    # Binary encoding for categorical variables
    binary_mappings = {
        'glucose_test': {'no': 0, 'normal': 1, 'high': 2},
        'A1Ctest': {'no': 0, 'normal': 1, 'high': 2},
        'change': {'no': 0, 'yes': 1},
        'diabetes_med': {'no': 0, 'yes': 1},
        'readmitted': {'no': 0, 'yes': 1}
    }
    
    for col, mapping in binary_mappings.items():
        df[col + '_encoded'] = df[col].map(mapping)
    
    # One-hot encode categorical variables with multiple categories
    categorical_cols = ['medical_specialty', 'diag_1', 'diag_2', 'diag_3']
    df_encoded = pd.get_dummies(df, columns=categorical_cols, prefix=categorical_cols)
    
    # Select features for the model
    feature_cols = ['age_numeric', 'time_in_hospital', 'n_lab_procedures', 
                   'n_procedures', 'n_medications', 'n_outpatient', 
                   'n_inpatient', 'n_emergency', 'glucose_test_encoded',
                   'A1Ctest_encoded', 'change_encoded', 'diabetes_med_encoded']
    
    # Add one-hot encoded columns
    onehot_cols = [col for col in df_encoded.columns if any(cat in col for cat in categorical_cols)]
    feature_cols.extend(onehot_cols)
    
    # Prepare features and target
    X = df_encoded[feature_cols].fillna(0)
    y = df_encoded['readmitted_encoded']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Create preprocessing pipeline
    numeric_features = ['age_numeric', 'time_in_hospital', 'n_lab_procedures', 
                       'n_procedures', 'n_medications', 'n_outpatient', 
                       'n_inpatient', 'n_emergency', 'glucose_test_encoded',
                       'A1Ctest_encoded', 'change_encoded', 'diabetes_med_encoded']
    
    # Preprocessing for numeric data
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    # Bundle preprocessing for numeric and categorical data
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', 'passthrough', onehot_cols)
        ]
    )
    
    # Create the full pipeline
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            class_weight='balanced'
        ))
    ])
    
    # Train the model
    print("Training model...")
    model_pipeline.fit(X_train, y_train)
    
    # Evaluate the model
    print("Evaluating model...")
    y_pred = model_pipeline.predict(X_test)
    y_pred_proba = model_pipeline.predict_proba(X_test)[:, 1]
    
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"ROC AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")
    
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Save the pipeline
    pipeline_path = 'models/readmit_pipeline.joblib'
    joblib.dump(model_pipeline, pipeline_path)
    print(f"Model pipeline saved to {pipeline_path}")
    
    # Save feature names for later use
    feature_names = X.columns.tolist()
    joblib.dump(feature_names, 'models/feature_names.joblib')
    print("Feature names saved to models/feature_names.joblib")
    
    # Save feature importance
    feature_importance = model_pipeline.named_steps['classifier'].feature_importances_
    importance_dict = dict(zip(feature_names, feature_importance))
    joblib.dump(importance_dict, 'models/feature_importance.joblib')
    print("Feature importance saved to models/feature_importance.joblib")
    
    return model_pipeline, feature_names, importance_dict

if __name__ == "__main__":
    pipeline, features, importance = create_model_pipeline()
    print("Model training completed successfully!")
