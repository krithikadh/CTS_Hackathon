#!/usr/bin/env python3
"""
Unit tests for the Hospital Readmission Prediction API.
Tests both JSON and image prediction endpoints.
"""

import unittest
import json
import io
import os
import sys
from PIL import Image

# Add backend directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app import app
from predictor import ReadmissionPredictor

class TestReadmissionAPI(unittest.TestCase):
    """Test cases for the readmission prediction API."""
    
    def setUp(self):
        """Set up test client and sample data."""
        self.app = app.test_client()
        self.app.testing = True
        
        # Sample patient data
        self.sample_patient_data = {
            "age": "[70-80)",
            "time_in_hospital": 8,
            "n_lab_procedures": 72,
            "n_procedures": 1,
            "n_medications": 18,
            "n_outpatient": 2,
            "n_inpatient": 0,
            "n_emergency": 0,
            "medical_specialty": "Missing",
            "diag_1": "Circulatory",
            "diag_2": "Respiratory",
            "diag_3": "Other",
            "glucose_test": "no",
            "A1Ctest": "no",
            "change": "no",
            "diabetes_med": "yes"
        }
    
    def test_health_endpoint(self):
        """Test the health check endpoint."""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('status', data)
        self.assertIn('timestamp', data)
    
    def test_json_prediction_valid_data(self):
        """Test JSON prediction with valid patient data."""
        response = self.app.post('/predict',
                                data=json.dumps(self.sample_patient_data),
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('readmit_probability', data)
        self.assertIn('prediction', data)
        self.assertIn('will_readmit', data)
        self.assertIn('risk_factors', data)
        
        # Check data types
        self.assertIsInstance(data['readmit_probability'], float)
        self.assertIsInstance(data['will_readmit'], bool)
        self.assertIsInstance(data['risk_factors'], list)
        
        # Check probability is between 0 and 1
        self.assertGreaterEqual(data['readmit_probability'], 0.0)
        self.assertLessEqual(data['readmit_probability'], 1.0)
    
    def test_json_prediction_missing_fields(self):
        """Test JSON prediction with missing required fields."""
        incomplete_data = {
            "age": "[70-80)",
            "time_in_hospital": 8
            # Missing other required fields
        }
        
        response = self.app.post('/predict',
                                data=json.dumps(incomplete_data),
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('Missing required fields', data['error'])
    
    def test_json_prediction_invalid_json(self):
        """Test JSON prediction with invalid JSON data."""
        response = self.app.post('/predict',
                                data='invalid json',
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
    
    def create_test_image(self):
        """Create a test image for multipart requests."""
        # Create a simple test image
        img = Image.new('RGB', (300, 200), color='white')
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return img_io
    
    def test_image_prediction_with_json(self):
        """Test image prediction with JSON patient data."""
        img_io = self.create_test_image()
        
        data = {
            'image': (img_io, 'test_image.png'),
            'json': json.dumps(self.sample_patient_data)
        }
        
        response = self.app.post('/predict',
                                data=data,
                                content_type='multipart/form-data')
        
        self.assertEqual(response.status_code, 200)
        
        response_data = json.loads(response.data)
        self.assertIn('readmit_probability', response_data)
        self.assertIn('prediction', response_data)
        self.assertIn('image_processed', response_data)
        self.assertIn('original_filename', response_data)
    
    def test_image_prediction_without_json(self):
        """Test image prediction without JSON data (uses defaults)."""
        img_io = self.create_test_image()
        
        data = {
            'image': (img_io, 'test_image.png')
        }
        
        response = self.app.post('/predict',
                                data=data,
                                content_type='multipart/form-data')
        
        self.assertEqual(response.status_code, 200)
        
        response_data = json.loads(response.data)
        self.assertIn('readmit_probability', response_data)
        self.assertIn('prediction', response_data)
        self.assertIn('image_processed', response_data)
    
    def test_image_prediction_invalid_json(self):
        """Test image prediction with invalid JSON in form data."""
        img_io = self.create_test_image()
        
        data = {
            'image': (img_io, 'test_image.png'),
            'json': 'invalid json'
        }
        
        response = self.app.post('/predict',
                                data=data,
                                content_type='multipart/form-data')
        
        self.assertEqual(response.status_code, 400)
        
        response_data = json.loads(response.data)
        self.assertIn('error', response_data)
        self.assertIn('Invalid JSON', response_data['error'])
    
    def test_invalid_request_format(self):
        """Test prediction endpoint with invalid request format."""
        response = self.app.post('/predict',
                                data='plain text',
                                content_type='text/plain')
        
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('Invalid request format', data['error'])
    
    def test_404_endpoint(self):
        """Test accessing non-existent endpoint."""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('Endpoint not found', data['error'])

class TestReadmissionPredictor(unittest.TestCase):
    """Test cases for the ReadmissionPredictor class."""
    
    def setUp(self):
        """Set up predictor instance."""
        # Note: This assumes the model files exist
        # In a real test environment, you might want to create mock models
        self.predictor = ReadmissionPredictor()
        
        self.sample_patient_data = {
            "age": "[70-80)",
            "time_in_hospital": 8,
            "n_lab_procedures": 72,
            "n_procedures": 1,
            "n_medications": 18,
            "n_outpatient": 2,
            "n_inpatient": 0,
            "n_emergency": 0,
            "medical_specialty": "Missing",
            "diag_1": "Circulatory",
            "diag_2": "Respiratory",
            "diag_3": "Other",
            "glucose_test": "no",
            "A1Ctest": "no",
            "change": "no",
            "diabetes_med": "yes"
        }
    
    def test_preprocess_input(self):
        """Test input preprocessing."""
        if self.predictor.model is None:
            self.skipTest("Model not available for testing")
        
        processed_df = self.predictor.preprocess_input(self.sample_patient_data)
        
        # Check that we get a DataFrame
        self.assertIsNotNone(processed_df)
        self.assertEqual(len(processed_df), 1)  # Should have one row
        
        # Check that numeric features are present
        numeric_features = ['age_numeric', 'time_in_hospital', 'n_lab_procedures']
        for feature in numeric_features:
            self.assertIn(feature, processed_df.columns)
    
    def test_predict_functionality(self):
        """Test the prediction functionality."""
        if self.predictor.model is None:
            self.skipTest("Model not available for testing")
        
        result = self.predictor.predict(self.sample_patient_data)
        
        # Check required fields in result
        required_fields = ['readmit_probability', 'prediction', 'will_readmit', 'risk_factors']
        for field in required_fields:
            self.assertIn(field, result)
        
        # Check data types
        self.assertIsInstance(result['readmit_probability'], float)
        self.assertIsInstance(result['will_readmit'], bool)
        self.assertIsInstance(result['risk_factors'], list)
        
        # Check probability bounds
        self.assertGreaterEqual(result['readmit_probability'], 0.0)
        self.assertLessEqual(result['readmit_probability'], 1.0)
    
    def test_format_feature_name(self):
        """Test feature name formatting."""
        # Test basic feature names
        self.assertEqual(
            self.predictor.format_feature_name('age_numeric'),
            'Patient Age'
        )
        
        self.assertEqual(
            self.predictor.format_feature_name('time_in_hospital'),
            'Length of Hospital Stay'
        )
        
        # Test one-hot encoded feature names
        self.assertEqual(
            self.predictor.format_feature_name('medical_specialty_Missing'),
            'Medical Specialty: Missing'
        )

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestReadmissionAPI))
    test_suite.addTest(unittest.makeSuite(TestReadmissionPredictor))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
