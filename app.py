#!/usr/bin/env python3
"""
Unified Flask API that uses the same predictor as backend/app.py
to return readmission predictions based on patient data.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from backend.predictor import ReadmissionPredictor

app = Flask(__name__)
CORS(app)

predictor = ReadmissionPredictor()
DEFAULT_DECISION_THRESHOLD = 0.50


def build_patient_data(payload: dict) -> dict:
    """Build a complete patient_data dict from either the full schema
    or a simplified schema sent by the frontend.
    """
    # If payload already includes all required fields, return as is
    required_fields = {
        'age', 'time_in_hospital', 'n_lab_procedures', 'n_procedures',
        'n_medications', 'n_outpatient', 'n_inpatient', 'n_emergency',
        'medical_specialty', 'diag_1', 'diag_2', 'diag_3',
        'glucose_test', 'A1Ctest', 'change', 'diabetes_med'
    }

    if required_fields.issubset(payload.keys()):
        return payload

    # Support legacy/simple schema
    age = payload.get('age') or payload.get('Age') or '70-80'
    if not (age.startswith('[') and age.endswith(')')):
        age = f"[{age})"

    diagnosis = payload.get('diagnosis') or []
    if isinstance(diagnosis, str):
        # allow comma-separated
        diagnosis = [d.strip() for d in diagnosis.split(',') if d.strip()]

    return {
        'age': age,
        'time_in_hospital': int(payload.get('visits') or payload.get('time_in_hospital') or 3),
        'n_lab_procedures': int(payload.get('lab_procedures') or payload.get('n_lab_procedures') or 40),
        'n_procedures': int(payload.get('procedures') or payload.get('n_procedures') or 1),
        'n_medications': int(payload.get('medications') or payload.get('n_medications') or 12),
        'n_outpatient': int(payload.get('outpatient_visits') or payload.get('n_outpatient') or 0),
        'n_inpatient': int(payload.get('previous_visits') or payload.get('n_inpatient') or 0),
        'n_emergency': int(payload.get('emergency_visits') or payload.get('n_emergency') or 0),
        'medical_specialty': payload.get('medical_specialty') or 'Missing',
        'diag_1': (diagnosis[0] if len(diagnosis) > 0 else payload.get('diag_1') or 'Other'),
        'diag_2': (diagnosis[1] if len(diagnosis) > 1 else payload.get('diag_2') or 'Other'),
        'diag_3': (diagnosis[2] if len(diagnosis) > 2 else payload.get('diag_3') or 'Other'),
        'glucose_test': payload.get('glucose') or payload.get('glucose_test') or 'no',
        'A1Ctest': payload.get('a1c') or payload.get('A1Ctest') or 'no',
        'change': payload.get('medication_changes') or payload.get('change') or 'no',
        'diabetes_med': payload.get('diabetes_med') or 'yes'
    }

@app.route("/health", methods=["GET"])
def health():
    try:
        return jsonify({
            "status": "healthy" if predictor.model is not None else "unhealthy",
            "model_loaded": predictor.model is not None,
            "timestamp": datetime.now().isoformat()
        }), 200 if predictor.model is not None else 503
    except Exception as e:
        return jsonify({"status": "unhealthy", "message": str(e)}), 503


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if not request.is_json:
            return jsonify({"error": "Expected JSON body"}), 400

        payload = request.get_json()

        patient_data = build_patient_data(payload)

        result = predictor.predict(patient_data)

        # Fixed decision rule: readmit if probability >= 0.50
        effective_threshold = DEFAULT_DECISION_THRESHOLD
        prob = float(result.get('readmit_probability', 0.0))
        will_readmit = prob >= effective_threshold
        result['will_readmit'] = bool(will_readmit)
        result['prediction'] = "WILL readmit" if will_readmit else "WILL NOT readmit"
        result['decision_threshold'] = effective_threshold

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
