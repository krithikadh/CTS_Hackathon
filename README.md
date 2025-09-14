# Hospital Readmission Prediction API

A comprehensive Flask-based API for predicting hospital readmissions using machine learning. This system provides both JSON and image-based prediction endpoints with risk factor analysis.

## Features

- **Machine Learning Pipeline**: Random Forest classifier with preprocessing pipeline
- **Dual API Support**: JSON requests and multipart requests with image overlay
- **Risk Factor Analysis**: Top 3 risk factors with feature importance
- **Image Processing**: Overlay predictions on uploaded medical images
- **Comprehensive Logging**: All predictions logged for audit purposes
- **Unit Tests**: Complete test suite for API endpoints

## Project Structure

```
CTS_Hackathon-main/
├── backend/
│   ├── app.py              # Flask application with endpoints
│   ├── predictor.py        # Model loading and prediction logic
│   ├── image_overlay.py    # Image processing with Pillow
│   └── requirements.txt    # Backend dependencies
├── models/
│   ├── readmit_pipeline.joblib    # Trained model pipeline
│   ├── feature_names.joblib       # Feature names for preprocessing
│   └── feature_importance.joblib  # Feature importance for risk factors
├── data/
│   └── hospital_readmissions.csv  # Training dataset
├── logs/
│   └── predictions.log     # Prediction logs
├── tests/
│   └── test_api.py        # Unit tests
├── train_model.py         # Model training script
└── README.md             # This file
```

## Installation & Setup

### 1. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Train the Model (if not already done)

```bash
cd ..
python train_model.py
```

### 3. Start the Flask API

```bash
cd backend
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check
```bash
GET /health
```

**Response:**
```json
{
    "status": "healthy",
    "message": "Hospital Readmission Prediction API is running",
    "model_loaded": true,
    "timestamp": "2025-09-13T15:38:00.000000"
}
```

### Prediction Endpoints

#### 1. JSON Prediction

```bash
POST /predict
Content-Type: application/json
```

**Request Body:**
```json
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
```

**Response:**
```json
{
    "readmit_probability": 0.65,
    "readmit_probability_percent": "65.0%",
    "prediction": "WILL readmit",
    "will_readmit": true,
    "risk_factors": [
        {
            "rank": 1,
            "factor": "Length of Hospital Stay",
            "contribution": "0.234",
            "impact": "High"
        },
        {
            "rank": 2,
            "factor": "Number of Medications",
            "contribution": "0.156",
            "impact": "High"
        },
        {
            "rank": 3,
            "factor": "Patient Age",
            "contribution": "0.089",
            "impact": "Medium"
        }
    ],
    "patient_data": { ... }
}
```

#### 2. Image Prediction with Overlay

```bash
POST /predict
Content-Type: multipart/form-data
```

**Form Data:**
- `image`: Image file (PNG, JPG, etc.)
- `json`: JSON string with patient data (optional)

**Response:**
```json
{
    "readmit_probability": 0.65,
    "readmit_probability_percent": "65.0%",
    "prediction": "WILL readmit",
    "will_readmit": true,
    "risk_factors": [...],
    "image_processed": true,
    "original_filename": "patient_chart.png",
    "patient_data": { ... }
}
```

## Example cURL Commands

### 1. Health Check
```bash
curl -X GET http://localhost:5000/health
```

### 2. JSON Prediction
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

### 3. Image Prediction with JSON Data
```bash
curl -X POST http://localhost:5000/predict \
  -F "image=@patient_chart.png" \
  -F 'json={
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
  }'
```

### 4. Image Prediction with Default Data
```bash
curl -X POST http://localhost:5000/predict \
  -F "image=@patient_chart.png"
```

## Field Descriptions

### Required Input Fields

| Field | Type | Description | Valid Values |
|-------|------|-------------|--------------|
| `age` | string | Patient age group | `[40-50)`, `[50-60)`, `[60-70)`, `[70-80)`, `[80-90)`, `[90-100)` |
| `time_in_hospital` | integer | Days spent in hospital | 1-14 |
| `n_lab_procedures` | integer | Number of lab procedures | 0-100+ |
| `n_procedures` | integer | Number of procedures | 0-10+ |
| `n_medications` | integer | Number of medications | 0-50+ |
| `n_outpatient` | integer | Outpatient visits | 0-20+ |
| `n_inpatient` | integer | Previous inpatient visits | 0-10+ |
| `n_emergency` | integer | Emergency visits | 0-10+ |
| `medical_specialty` | string | Medical specialty | Various specialties or "Missing" |
| `diag_1` | string | Primary diagnosis | "Circulatory", "Diabetes", "Respiratory", "Other", etc. |
| `diag_2` | string | Secondary diagnosis | Same as diag_1 |
| `diag_3` | string | Additional diagnosis | Same as diag_1 |
| `glucose_test` | string | Glucose test result | "no", "normal", "high" |
| `A1Ctest` | string | A1C test result | "no", "normal", "high" |
| `change` | string | Medication changes | "no", "yes" |
| `diabetes_med` | string | Diabetes medication | "no", "yes" |

## Image Overlay Features

When uploading an image, the API will:

1. **Process the uploaded image** using Pillow
2. **Add a semi-transparent overlay** in the top-right corner
3. **Display prediction information**:
   - Readmission probability percentage
   - Prediction result (WILL/WILL NOT readmit)
   - Top 3 risk factors
4. **Return both** the modified image data and JSON response

## Running Tests

```bash
cd tests
python test_api.py
```

The test suite includes:
- Health endpoint testing
- JSON prediction validation
- Image upload testing
- Error handling verification
- Model functionality tests

## Logging

All predictions are logged to `logs/predictions.log` with:
- Timestamp
- Request type (JSON/image)
- Patient data
- Prediction results
- Image filename (if applicable)

## Model Information

- **Algorithm**: Random Forest Classifier
- **Features**: 16 core features + one-hot encoded categorical variables
- **Training Data**: Hospital readmissions dataset with 25,000+ records
- **Performance**: Balanced accuracy with class weight handling
- **Risk Factors**: Calculated using feature importance from the trained model

## Error Handling

The API provides comprehensive error handling:
- **400**: Bad Request (missing fields, invalid JSON)
- **404**: Endpoint not found
- **500**: Internal server error
- **503**: Service unavailable (model not loaded)

## Development Notes

- The API uses CORS for cross-origin requests
- All endpoints return JSON responses
- Image processing is optional and gracefully degrades
- Model pipeline includes preprocessing for robust predictions
- Feature importance is used for risk factor calculation

## Future Enhancements

- SHAP integration for more detailed risk factor analysis
- Model versioning and A/B testing
- Database integration for prediction history
- Authentication and rate limiting
- Batch prediction endpoints
- Real-time model monitoring
