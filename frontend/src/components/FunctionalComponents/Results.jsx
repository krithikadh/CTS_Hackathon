import React from "react";
import "../css/Results.css";
import { Link } from "react-router-dom";

const Results = () => {
  return (
    <div className="results-container">
      <h1>Results</h1>
      <p>Prediction results will appear here.</p>

      <Link to="/" className="back-button">
        Back to Form
      </Link>
    </div>
  );
};

export default Results;

