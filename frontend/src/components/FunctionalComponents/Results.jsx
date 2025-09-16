import React, { useState, useEffect } from "react";
import { useLocation, Link } from "react-router-dom";
import axios from "axios";
import "../css/Results.css";

const Results = () => {
  const location = useLocation();
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPrediction = async () => {
      try {
        setLoading(true);
        setError(null);

        const formData = location.state?.formData;
        if (!formData) {
          setError("No patient data provided");
          setLoading(false);
          return;
        }

        const apiData = {
          age: `[${formData.age})`,
          time_in_hospital: parseInt(formData.visits) || 1,
          n_lab_procedures: parseInt(formData.lab_procedures) || 15,
          n_procedures: parseInt(formData.procedures) || 1,
          n_medications: parseInt(formData.medications) || 10,
          n_outpatient: parseInt(formData.previous_visits) || 0,
          n_inpatient: 0,
          n_emergency: parseInt(formData.emergency_visits) || 0,
          medical_specialty: formData.medical_specialty || "Missing",
          diag_1: formData.diagnosis[0] || "Other",
          diag_2: formData.diagnosis[1] || "Other",
          diag_3: formData.diagnosis[2] || "Other",
          glucose_test: formData.glucose || "no",
          A1Ctest: formData.a1c || "no",
          change: formData.medication_changes || "no",
          diabetes_med: "yes",
          name: formData.name || "Unknown",
        };

        const response = await axios.post("http://localhost:5000/predict", apiData, {
          headers: { "Content-Type": "application/json" },
        });

        // Ensure probability is a number
        const prob = Number(response.data.readmit_probability || 0);

        // Convert to percentage (0.67 -> "67%")
        const probPercent = `${(prob * 100).toFixed(2)}%`;

        // Risk calculation
        const will = prob >= 0.5;
        const riskLevel = will ? "High Risk" : "Low Risk";

        setPrediction({
          ...response.data,
          will_readmit: will,
          risk_level: riskLevel,
          readmit_probability_percent: probPercent,
          prediction: will ? <b>WILL readmit</b> : <b>WILL NOT readmit</b>,
          patient_name: formData.name || "Unknown",
        });
      } catch (err) {
        console.error("Prediction error:", err);
        setError(err.response?.data?.error || "Failed to get prediction");
      } finally {
        setLoading(false);
      }
    };

    fetchPrediction();
  }, [location.state]);

  if (loading) {
    return (
      <div className="page-container">
        <div className="info-section">
          <h1>Processing Prediction</h1>
          <p>Please wait while we analyze patient data...</p>
        </div>
        <div className="results-section">
          <div className="loading-box">
            <h2>Analyzing Patient Data...</h2>
            <div className="spinner"></div>
            <p>Please wait while we process the prediction.</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page-container">
        <div className="info-section">
          <h1>Prediction Error</h1>
          <p>We couldn’t process the patient data.</p>
        </div>
        <div className="results-section">
          <div className="error-box">
            <h2>Error</h2>
            <p>{error}</p>
            <Link to="/" className="back-button">
              Back to Form
            </Link>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="page-container">
      {/* Left Side (Info) */}
      <div className="info-section">
        <h1>Hospital Readmission Predictor</h1>
        <p>
          Below are the prediction results based on the entered patient details.
        </p>
      </div>

      {/* Right Side (Results) */}
      <div className="results-section">
        {prediction && (
          <>
            {/* Prediction Result */}
            <div
              className={`result-card ${
                prediction.will_readmit ? "danger" : "success"
              }`}
            >
              <h2>Prediction Result</h2>
              <h3>{prediction.prediction}</h3>
              <p>
                Readmission Probability:{" "}
                <span className="probability">
                  {prediction.readmit_probability_percent}
                </span>
              </p>
              <p>
                Risk Level:{" "}
                <span
                  className={
                    prediction.will_readmit ? "high-risk" : "low-risk"
                  }
                >
                  {prediction.risk_level}
                </span>
              </p>
            </div>

            {/* Patient Info */}
            <div className="result-card info">
              <h3>Patient Information</h3>
              <ul className="patient-list">
                <li>Name: {prediction.patient_name}</li>
                <li>Age Group: {prediction.patient_data.age}</li>
                <li>
                  Days at Hospital: {prediction.patient_data.time_in_hospital}
                </li>
                <li>Diagnosis: {prediction.patient_data.diag_1}</li>
                <li>Glucose Test: {prediction.patient_data.glucose_test}</li>
                <li>A1C Test: {prediction.patient_data.A1Ctest}</li>
              </ul>
            </div>

            {/* Clinical Recommendations */}
            <div
              className={`result-card ${
                prediction.will_readmit ? "danger" : "success"
              }`}
            >
              <h3>Clinical Recommendations</h3>
              {prediction.will_readmit ? (
                <ul>
                  <li>Schedule follow-up appointment within 7 days</li>
                  <li>Ensure medication adherence counseling</li>
                  <li>Consider home health services</li>
                  <li>Review discharge planning with care team</li>
                  <li>Monitor top risk factors closely</li>
                </ul>
              ) : (
                <ul>
                  <li>Standard discharge planning</li>
                  <li>Follow-up appointment within 2-4 weeks</li>
                  <li>Patient education on warning signs</li>
                  <li>Continue current treatment plan</li>
                </ul>
              )}
            </div>

            {/* Action Buttons */}
            <div className="button-group">
              <Link to="/" className="btn primary">
                New Prediction
              </Link>
              <button className="btn secondary" onClick={() => window.print()}>
                Print Results
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default Results;
