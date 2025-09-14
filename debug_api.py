#!/usr/bin/env python3
"""
Debug script to test the Flask API components individually.
"""

import sys
import os
sys.path.append('backend')

def test_predictor():
    """Test the predictor module."""
    try:
        from backend.predictor import ReadmissionPredictor
        
        print("Testing predictor...")
        predictor = ReadmissionPredictor()
        
        if predictor.model is None:
            print("ERROR: Model not loaded")
            return False
        
        test_data = {
            'age': '[70-80)',
            'time_in_hospital': 8,
            'n_lab_procedures': 72,
            'n_procedures': 1,
            'n_medications': 18,
            'n_outpatient': 2,
            'n_inpatient': 0,
            'n_emergency': 0,
            'medical_specialty': 'Missing',
            'diag_1': 'Circulatory',
            'diag_2': 'Respiratory',
            'diag_3': 'Other',
            'glucose_test': 'no',
            'A1Ctest': 'no',
            'change': 'no',
            'diabetes_med': 'yes'
        }
        
        result = predictor.predict(test_data)
        print(f"Prediction successful: {result['prediction']}")
        print(f"Probability: {result['readmit_probability_percent']}")
        return True
        
    except Exception as e:
        print(f"Predictor error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_flask_app():
    """Test Flask app initialization."""
    try:
        import sys
        sys.path.append('backend')
        from backend.app import app
        
        with app.test_client() as client:
            # Test health endpoint
            response = client.get('/health')
            print(f"Health endpoint status: {response.status_code}")
            
            # Test prediction endpoint
            test_data = {
                'age': '[70-80)',
                'time_in_hospital': 8,
                'n_lab_procedures': 72,
                'n_procedures': 1,
                'n_medications': 18,
                'n_outpatient': 2,
                'n_inpatient': 0,
                'n_emergency': 0,
                'medical_specialty': 'Missing',
                'diag_1': 'Circulatory',
                'diag_2': 'Respiratory',
                'diag_3': 'Other',
                'glucose_test': 'no',
                'A1Ctest': 'no',
                'change': 'no',
                'diabetes_med': 'yes'
            }
            
            response = client.post('/predict', json=test_data)
            print(f"Prediction endpoint status: {response.status_code}")
            
            if response.status_code != 200:
                print(f"Error response: {response.get_data(as_text=True)}")
            else:
                print("Prediction endpoint working correctly")
                
        return True
        
    except Exception as e:
        print(f"Flask app error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("DEBUGGING FLASK API")
    print("=" * 50)
    
    print("\n1. Testing Predictor Module...")
    predictor_ok = test_predictor()
    
    print("\n2. Testing Flask App...")
    flask_ok = test_flask_app()
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Predictor: {'✓ OK' if predictor_ok else '✗ FAILED'}")
    print(f"Flask App: {'✓ OK' if flask_ok else '✗ FAILED'}")
