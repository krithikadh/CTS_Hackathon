#!/usr/bin/env python3
"""
Simple test script to demonstrate the Flask API functionality.
"""

import requests
import json
from PIL import Image
import io

# API base URL
BASE_URL = "http://localhost:5000"

def test_health_endpoint():
    """Test the health check endpoint."""
    print("Testing /health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_json_prediction():
    """Test JSON prediction endpoint."""
    print("\nTesting /predict endpoint with JSON...")
    
    sample_data = {
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
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json=sample_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Prediction: {result['prediction']}")
            print(f"Probability: {result['readmit_probability_percent']}")
            print("Risk Factors:")
            for factor in result['risk_factors']:
                print(f"  {factor['rank']}. {factor['factor']} ({factor['impact']} impact)")
        else:
            print(f"Error Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def create_test_image():
    """Create a simple test image."""
    img = Image.new('RGB', (400, 300), color='lightblue')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

def test_image_prediction():
    """Test image prediction endpoint."""
    print("\nTesting /predict endpoint with image...")
    
    sample_data = {
        "age": "[60-70)",
        "time_in_hospital": 5,
        "n_lab_procedures": 45,
        "n_procedures": 2,
        "n_medications": 12,
        "n_outpatient": 1,
        "n_inpatient": 1,
        "n_emergency": 0,
        "medical_specialty": "InternalMedicine",
        "diag_1": "Diabetes",
        "diag_2": "Circulatory",
        "diag_3": "Other",
        "glucose_test": "high",
        "A1Ctest": "high",
        "change": "yes",
        "diabetes_med": "yes"
    }
    
    try:
        # Create test image
        test_img = create_test_image()
        
        files = {
            'image': ('test_patient.png', test_img, 'image/png'),
            'json': (None, json.dumps(sample_data))
        }
        
        response = requests.post(f"{BASE_URL}/predict", files=files)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Prediction: {result['prediction']}")
            print(f"Probability: {result['readmit_probability_percent']}")
            print(f"Image Processed: {result.get('image_processed', False)}")
            print("Risk Factors:")
            for factor in result['risk_factors']:
                print(f"  {factor['rank']}. {factor['factor']} ({factor['impact']} impact)")
        else:
            print(f"Error Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("Hospital Readmission Prediction API Test")
    print("=" * 60)
    
    tests = [
        ("Health Check", test_health_endpoint),
        ("JSON Prediction", test_json_prediction),
        ("Image Prediction", test_image_prediction)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'-' * 40}")
        success = test_func()
        results.append((test_name, success))
        print(f"{test_name}: {'✓ PASSED' if success else '✗ FAILED'}")
    
    print(f"\n{'=' * 60}")
    print("TEST SUMMARY")
    print(f"{'=' * 60}")
    for test_name, success in results:
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"{test_name:<20}: {status}")
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    print(f"\nOverall: {passed}/{total} tests passed")

if __name__ == "__main__":
    main()
