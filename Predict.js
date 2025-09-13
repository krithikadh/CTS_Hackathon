
import React, { useState } from "react";

function Predict() {
  const [features, setFeatures] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ features: features.split(",").map(Number) }),
    });

    const data = await response.json();
    setResult(data.prediction);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Hospital Readmission Prediction</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter features comma separated"
          value={features}
          onChange={(e) => setFeatures(e.target.value)}
          style={{ width: "300px" }}
        />
        <button type="submit">Predict</button>
      </form>
      {result && <h3>Prediction: {result}</h3>}
    </div>
  );
}

export default Predict;
