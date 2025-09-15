import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../css/FormPage.css";

const FormPage = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    age: "",
    visits: "1",
    diagnosis: [],
    glucose: "",
    aic: "",
    medications: "5",
    lab_procedures: "15",
    procedures: "1",
    previous_visits: "0",
    emergency_visits: "0",
    medication_changes: "no"
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleDiagnosisChange = (e) => {
    const { value } = e.target;
    setFormData((prev) => {
      if (prev.diagnosis.includes(value)) {
        return {
          ...prev,
          diagnosis: prev.diagnosis.filter((d) => d !== value),
        };
      }
      if (prev.diagnosis.length < 3) {
        return { ...prev, diagnosis: [...prev.diagnosis, value] };
      }
      return prev;
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitted Data:", formData);
    navigate("/results", { state: { formData } });
  };

  return (
    <div className="form-container">
      <h2>Patient Details Form</h2>
      <form onSubmit={handleSubmit}>
        <label>Age:</label>
        <select name="age" value={formData.age} onChange={handleChange}>
          <option value="">--Select Age--</option>
          <option value="40-50">40-50</option>
          <option value="50-60">50-60</option>
          <option value="60-70">60-70</option>
          <option value="70-80">70-80</option>
          <option value="80-90">80-90</option>
          <option value="90-100">90-100</option>
        </select>

        <label>Hospital Stay (days):</label>
        <input
          type="number"
          name="visits"
          value={formData.visits}
          onChange={handleChange}
          min="1"
          max="30"
        />


        <label>Diagnosis (choose up to 3):</label>
        <div className="diagnosis-options">
          {[
            "Circulatory",
            "Diabetes",
            "Digestive",
            "Injury",
            "Musculoskeletal",
            "Respiratory",
            "Other",
          ].map((d, index) => (
            <label key={d} className="checkbox-label">
              <input
                type="checkbox"
                id={`diagnosis-${index}`}
                value={d}
                checked={formData.diagnosis.includes(d)}
                onChange={handleDiagnosisChange}
              />
              {d}
            </label>
          ))}
        </div>

        <label>Glucose Test:</label>
        <select name="glucose" value={formData.glucose} onChange={handleChange}>
          <option value="">--Select Level--</option>
          <option value="high">High</option>
          <option value="normal">Normal</option>
          <option value="unknown">Unknown</option>
        </select>

        <label>A1C Test:</label>
        <select name="a1c" value={formData.a1c} onChange={handleChange}>
          <option value="">--Select Level--</option>
          <option value="high">High</option>
          <option value="normal">Normal</option>
          <option value="unknown">Unknown</option>
        </select>

        <label>Number of Medications:</label>
        <input
          type="number"
          name="medications"
          value={formData.medications}
          onChange={handleChange}
          min="1"
          max="50"
        />

        <label>Lab Procedures Count:</label>
        <input
          type="number"
          name="lab_procedures"
          value={formData.lab_procedures}
          onChange={handleChange}
          min="1"
          max="200"
        />

        <label>Number of Procedures:</label>
        <input
          type="number"
          name="procedures"
          value={formData.procedures}
          onChange={handleChange}
          min="0"
          max="20"
        />

        <label>Previous Outpatient Visits:</label>
        <input
          type="number"
          name="previous_visits"
          value={formData.previous_visits}
          onChange={handleChange}
          min="0"
          max="10"
        />

        <label>Emergency Visits:</label>
        <input
          type="number"
          name="emergency_visits"
          value={formData.emergency_visits}
          onChange={handleChange}
          min="0"
          max="10"
        />

        <label>Medication Changes:</label>
        <select name="medication_changes" value={formData.medication_changes} onChange={handleChange}>
          <option value="no">No Changes</option>
          <option value="yes">Has Changes</option>
        </select>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default FormPage;
