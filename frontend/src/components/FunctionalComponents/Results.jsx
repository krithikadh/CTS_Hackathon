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

        // Get form data from navigation state
        const formData = location.state?.formData;
        
        if (!formData) {
          setError("No patient data provided");
          setLoading(false);
          return;
        }

        // Map form data to API format
        const apiData = {
          age: `[${formData.age})`,  // Format as [XX-YY) for the API
          time_in_hospital: parseInt(formData.visits) || 1,
          n_lab_procedures: 15,  // Default value
          n_procedures: 1,  // Default value
          n_medications: 10,  // Default value
          n_outpatient: 0,  // Default values for these fields
          n_inpatient: 0,
          n_emergency: 0,
          medical_specialty: "Missing",
          diag_1: formData.diagnosis[0] || "Other",
          diag_2: formData.diagnosis[1] || "Other", 
          diag_3: formData.diagnosis[2] || "Other",
          glucose_test: formData.glucose || "no",
          A1Ctest: formData.aic || "no",
          change: "no",
          diabetes_med: "yes"
        };

        // Call Flask API
        const response = await axios.post('http://localhost:5000/predict', apiData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });

        setPrediction(response.data);
      } catch (err) {
        console.error('Prediction error:', err);
        setError(err.response?.data?.error || 'Failed to get prediction');
      } finally {
        setLoading(false);
      }
    };

    fetchPrediction();
  }, [location.state]);

  if (loading) {
    return (
      <div className="results-container">
        <div className="loading">
          <h2>Analyzing Patient Data...</h2>
          <div className="spinner"></div>
          <p>Please wait while we process the prediction.</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="results-container">
        <div className="error">
          <h2>Error</h2>
          <p>{error}</p>
          <Link to="/" className="back-button">
            Back to Form
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="container-fluid bg-light min-vh-100">
      {/* Professional Header */}
      <div className="bg-primary text-white py-4 mb-4">
        <div className="container">
          <div className="row">
            <div className="col-12 text-center">
              <h1 className="display-4 fw-bold mb-2">Patient Readmission Risk Prediction</h1>
              <p className="lead mb-0">Advanced Healthcare Analytics System</p>
            </div>
          </div>
        </div>
      </div>
      
      <div className="container">
      
      {prediction && (
        <div className="row g-4">
          {/* Main Prediction Card */}
          <div className="col-12">
            <div className="card shadow-lg border-0">
              <div className={`card-header text-white ${prediction.will_readmit ? 'bg-danger' : 'bg-success'}`}>
                <h2 className="card-title mb-0 text-center">
                  <i className={`bi ${prediction.will_readmit ? 'bi-exclamation-triangle-fill' : 'bi-check-circle-fill'} me-2`}></i>
                  Prediction Result
                </h2>
              </div>
              <div className="card-body text-center p-5">
                <div className={`alert ${prediction.will_readmit ? 'alert-danger' : 'alert-success'} border-0 shadow-sm`}>
                  <h3 className="display-5 fw-bold mb-3">{prediction.prediction}</h3>
                  <div className="d-flex justify-content-center align-items-center">
                    <span className="fs-4 me-3">Readmission Probability:</span>
                    <span className={`badge ${prediction.will_readmit ? 'bg-danger' : 'bg-success'} fs-3 px-4 py-2`}>
                      {prediction.readmit_probability_percent}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Risk Factors Card */}
          <div className="col-lg-8 col-12">
            <div className="card shadow-lg border-0">
              <div className="card-header bg-warning text-dark">
                <h3 className="card-title mb-0">
                  <i className="bi bi-graph-up-arrow me-2"></i>
                  Top Risk Factors
                </h3>
              </div>
              <div className="card-body p-4">
                {prediction.risk_factors && prediction.risk_factors.length > 0 ? (
                  <div className="table-responsive">
                    <table className="table table-hover">
                      <thead className="table-dark">
                        <tr>
                          <th scope="col" className="text-center">#</th>
                          <th scope="col">Risk Factor</th>
                          <th scope="col" className="text-center">Impact Level</th>
                          <th scope="col" className="text-center">Contribution</th>
                        </tr>
                      </thead>
                      <tbody>
                        {prediction.risk_factors.map((factor, index) => (
                          <tr key={index} className={`table-${factor.impact.toLowerCase() === 'high' ? 'danger' : factor.impact.toLowerCase() === 'medium' ? 'warning' : 'info'}`}>
                            <td className="text-center">
                              <span className={`badge rounded-pill ${factor.impact.toLowerCase() === 'high' ? 'bg-danger' : factor.impact.toLowerCase() === 'medium' ? 'bg-warning text-dark' : 'bg-info'} fs-6`}>
                                {factor.rank}
                              </span>
                            </td>
                            <td className="fw-semibold">{factor.factor}</td>
                            <td className="text-center">
                              <span className={`badge ${factor.impact.toLowerCase() === 'high' ? 'bg-danger' : factor.impact.toLowerCase() === 'medium' ? 'bg-warning text-dark' : 'bg-info'}`}>
                                <i className={`bi ${factor.impact.toLowerCase() === 'high' ? 'bi-exclamation-triangle-fill' : factor.impact.toLowerCase() === 'medium' ? 'bi-exclamation-circle-fill' : 'bi-info-circle-fill'} me-1`}></i>
                                {factor.impact}
                              </span>
                            </td>
                            <td className="text-center text-muted">{factor.contribution}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                ) : (
                  <div className="alert alert-info text-center">
                    <i className="bi bi-info-circle me-2"></i>
                    No specific risk factors identified.
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Patient Data Summary */}
          <div className="col-lg-4 col-12">
            <div className="card shadow-lg border-0">
              <div className="card-header bg-info text-white">
                <h3 className="card-title mb-0">
                  <i className="bi bi-person-fill me-2"></i>
                  Patient Information
                </h3>
              </div>
              <div className="card-body p-4">
                <div className="list-group list-group-flush">
                  <div className="list-group-item d-flex justify-content-between align-items-center border-0 px-0">
                    <strong className="text-muted">Age Group:</strong>
                    <span className="badge bg-secondary fs-6">{prediction.patient_data.age}</span>
                  </div>
                  <div className="list-group-item d-flex justify-content-between align-items-center border-0 px-0">
                    <strong className="text-muted">Hospital Stay:</strong>
                    <span className="badge bg-secondary fs-6">{prediction.patient_data.time_in_hospital} days</span>
                  </div>
                  <div className="list-group-item d-flex justify-content-between align-items-center border-0 px-0">
                    <strong className="text-muted">Primary Diagnosis:</strong>
                    <span className="badge bg-secondary fs-6">{prediction.patient_data.diag_1}</span>
                  </div>
                  <div className="list-group-item d-flex justify-content-between align-items-center border-0 px-0">
                    <strong className="text-muted">Glucose Test:</strong>
                    <span className={`badge fs-6 ${prediction.patient_data.glucose_test === 'high' ? 'bg-danger' : prediction.patient_data.glucose_test === 'normal' ? 'bg-success' : 'bg-secondary'}`}>
                      {prediction.patient_data.glucose_test}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Recommendations */}
          <div className="col-12">
            <div className="card shadow-lg border-0">
              <div className={`card-header text-white ${prediction.will_readmit ? 'bg-danger' : 'bg-success'}`}>
                <h3 className="card-title mb-0">
                  <i className="bi bi-clipboard-check me-2"></i>
                  Clinical Recommendations
                </h3>
              </div>
              <div className="card-body p-4">
                {prediction.will_readmit ? (
                  <div className={`alert alert-danger border-0 shadow-sm`}>
                    <h4 className="alert-heading">
                      <i className="bi bi-exclamation-triangle-fill me-2"></i>
                      High Risk Patient - Immediate Actions Required:
                    </h4>
                    <hr />
                    <ul className="mb-0 fs-6">
                      <li className="mb-2"><i className="bi bi-calendar-check text-danger me-2"></i>Schedule follow-up appointment within 7 days</li>
                      <li className="mb-2"><i className="bi bi-capsule text-danger me-2"></i>Ensure medication adherence counseling</li>
                      <li className="mb-2"><i className="bi bi-house-heart text-danger me-2"></i>Consider home health services</li>
                      <li className="mb-2"><i className="bi bi-clipboard-data text-danger me-2"></i>Review discharge planning with care team</li>
                      <li className="mb-0"><i className="bi bi-graph-up text-danger me-2"></i>Monitor top risk factors closely</li>
                    </ul>
                  </div>
                ) : (
                  <div className={`alert alert-success border-0 shadow-sm`}>
                    <h4 className="alert-heading">
                      <i className="bi bi-check-circle-fill me-2"></i>
                      Low Risk Patient - Standard Care Protocol:
                    </h4>
                    <hr />
                    <ul className="mb-0 fs-6">
                      <li className="mb-2"><i className="bi bi-clipboard text-success me-2"></i>Standard discharge planning</li>
                      <li className="mb-2"><i className="bi bi-calendar text-success me-2"></i>Follow-up appointment within 2-4 weeks</li>
                      <li className="mb-2"><i className="bi bi-book text-success me-2"></i>Patient education on warning signs</li>
                      <li className="mb-0"><i className="bi bi-arrow-repeat text-success me-2"></i>Continue current treatment plan</li>
                    </ul>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
      
      {/* Action Buttons */}
      <div className="row mt-5">
        <div className="col-12 text-center">
          <div className="d-flex justify-content-center gap-3 flex-wrap">
            <Link to="/" className="btn btn-primary btn-lg px-5 py-3">
              <i className="bi bi-plus-circle me-2"></i>
              New Prediction
            </Link>
            <button 
              className="btn btn-outline-secondary btn-lg px-5 py-3" 
              onClick={() => window.print()}
            >
              <i className="bi bi-printer me-2"></i>
              Print Results
            </button>
          </div>
        </div>
      </div>
      </div>
    </div>
  );
};

export default Results;

