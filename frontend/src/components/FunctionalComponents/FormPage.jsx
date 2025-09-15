import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../css/FormPage.css";

const FormPage = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    gender: "",
    age: "",
    visits: "1",
    diagnosis: [],
    glucose: "",
    a1c: "",
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
    <div className="page-container">
      {/* Left Section */}
      <div className="info-section">
        <h1>Hospital Readmission Predictor</h1>
        <p>
          Our system helps predict the chances of hospital readmission based on
          patient details and medical history. 
        </p>
        <p>
          This tool assists healthcare providers in improving patient care,
          planning follow-ups, and reducing readmission rates.
        </p>
        <p>
          Fill in the form to get an instant prediction and insights about the
          patient’s readmission probability.
        </p>
      </div>

      {/* Right Section */}
      <div className="form-section">
        <h2>Patient Details Form</h2>
        <form onSubmit={handleSubmit}>
          <label>Full Name:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Enter patient name"
            required
          />

          <label>Gender:</label>
          <select
            name="gender"
            value={formData.gender}
            onChange={handleChange}
            required
          >
            <option value="">--Select Gender--</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>

          <label>Age:</label>
          <select
            name="age"
            value={formData.age}
            onChange={handleChange}
            required
          >
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
          <select
            name="glucose"
            value={formData.glucose}
            onChange={handleChange}
            required
          >
            <option value="">--Select Level--</option>
            <option value="high">High</option>
            <option value="normal">Normal</option>
            <option value="unknown">Unknown</option>
          </select>

          <label>A1C Test:</label>
          <select
            name="a1c"
            value={formData.a1c}
            onChange={handleChange}
            required
          >
            <option value="">--Select Level--</option>
            <option value="high">High</option>
            <option value="normal">Normal</option>
            <option value="unknown">Unknown</option>
          </select>

          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
};

export default FormPage;
