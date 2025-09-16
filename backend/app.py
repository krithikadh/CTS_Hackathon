from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import logging
import os
import io
from datetime import datetime
from predictor import ReadmissionPredictor
from image_overlay import ImageOverlay

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
logs_dir = os.path.join(project_root, 'logs')
os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(logs_dir, 'predictions.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
predictor = ReadmissionPredictor()
image_overlay = ImageOverlay()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    try:
        if predictor.model is None:
            return jsonify({
                'status': 'unhealthy',
                'message': 'Model not loaded',
                'timestamp': datetime.now().isoformat()
            }), 503
        
        return jsonify({
            'status': 'healthy',
            'message': 'Hospital Readmission Prediction API is running',
            'model_loaded': True,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            'status': 'unhealthy',
            'message': str(e),
            'timestamp': datetime.now().isoformat()
        }), 503

@app.route('/predict', methods=['POST'])
def predict():
    """
    Prediction endpoint supporting both JSON and multipart requests.
    
    JSON Request:
    {
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
    
    Multipart Request:
    - image: uploaded image file
    - json: JSON string with patient data (optional)
    """
    
    try:
        if 'image' in request.files:
            return handle_image_prediction(request)
    
        elif request.is_json:
            return handle_json_prediction(request)
        
        else:
            return jsonify({
                'error': 'Invalid request format. Expected JSON or multipart with image.',
                'timestamp': datetime.now().isoformat()
            }), 400
    
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        return jsonify({
            'error': f'Prediction failed: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500

def handle_json_prediction(request):
    """Handle JSON prediction request."""
    patient_data = request.get_json()
    

    required_fields = [
        'age', 'time_in_hospital', 'n_lab_procedures', 'n_procedures',
        'n_medications', 'n_outpatient', 'n_inpatient', 'n_emergency',
        'medical_specialty', 'diag_1', 'diag_2', 'diag_3',
        'glucose_test', 'A1Ctest', 'change', 'diabetes_med'
    ]
    
    missing_fields = [field for field in required_fields if field not in patient_data]
    if missing_fields:
        return jsonify({
            'error': f'Missing required fields: {missing_fields}',
            'timestamp': datetime.now().isoformat()
        }), 400
    
   
    result = predictor.predict(patient_data)
    
    log_prediction(patient_data, result, 'json')
    
    return jsonify(result), 200

def handle_image_prediction(request):
    """Handle multipart prediction request with image."""
    image_file = request.files['image']
    
    patient_data = {}
    if 'json' in request.form:
        import json
        try:
            patient_data = json.loads(request.form['json'])
        except json.JSONDecodeError:
            return jsonify({
                'error': 'Invalid JSON in form data',
                'timestamp': datetime.now().isoformat()
            }), 400

    if not patient_data:
        patient_data = get_default_patient_data()
    
    result = predictor.predict(patient_data)
    
    try:
        image_file.seek(0)
        image_data = image_file.read()
        
        modified_image = image_overlay.add_prediction_overlay(image_data, result)
        
        log_prediction(patient_data, result, 'image', image_file.filename)
        
        img_io = io.BytesIO()
        modified_image.save(img_io, 'PNG')
        img_io.seek(0)
        
        result['image_processed'] = True
        result['original_filename'] = image_file.filename
        
        return jsonify(result), 200
        
    except Exception as e:
        logger.error(f"Image processing failed: {str(e)}")
        result['image_processed'] = False
        result['image_error'] = str(e)
        return jsonify(result), 200

def get_default_patient_data():
    """Return default patient data for demo purposes."""
    return {
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

def log_prediction(patient_data, result, request_type, filename=None):
    """Log prediction details."""
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'request_type': request_type,
        'patient_data': patient_data,
        'prediction': result,
        'filename': filename
    }
    
    logger.info(f"Prediction made: {log_entry}")

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'message': 'Available endpoints: /health, /predict',
        'timestamp': datetime.now().isoformat()
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'message': 'Please check the logs for more details',
        'timestamp': datetime.now().isoformat()
    }), 500

if __name__ == '__main__':
    os.makedirs('../logs', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
