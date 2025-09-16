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
    medications: "0",
    lab_procedures: "0",
    procedures: "0",
    previous_visits: "0",
    emergency_visits: "0",
    medication_changes: "no",
    medical_specialty: "Missing"
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
      Hospital Readmission Predictor is an AI-powered web application designed
      to help healthcare providers assess the likelihood of a patient being
      readmitted after discharge. By analyzing patient demographics, medical
      history, and clinical details, the system provides instant predictions
      and actionable insights.
    </p>
    <p>
      This tool supports doctors, nurses, and hospital administrators in:
    </p>
    <ul>
      <li>Improving patient care through early identification of high-risk patients.</li>
      <li>Optimizing treatment plans by tailoring follow-ups and preventive measures.</li>
      <li>Reducing hospital costs by lowering avoidable readmission rates.</li>
      <li>Supporting decision-making with data-driven insights.</li>
    </ul>
    <p>
      With its intuitive interface, healthcare professionals can enter patient
      details via a user-friendly form and instantly receive a prediction,
      along with probability scores and key contributing factors.
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

          <label>Diagnosis (select up to 3 and give primary first):</label>
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

          <label>Medical Specialty:</label>
          <select name="medical_specialty" value={formData.medical_specialty} onChange={handleChange}>
            {[
              "Missing",
              "InternalMedicine",
              "Family/GeneralPractice",
              "Cardiology",
              "Endocrinology",
              "Other"
            ].map(opt => (
              <option key={opt} value={opt}>{opt}</option>
            ))}
          </select>

          <label>Number of Medications:</label>
          <input type="number" name="medications" min="0" max="50" value={formData.medications} onChange={handleChange} />

          <label>Lab Procedures:</label>
          <input type="number" name="lab_procedures" min="0" max="200" value={formData.lab_procedures} onChange={handleChange} />

          <label>Number of Procedures:</label>
          <input type="number" name="procedures" min="0" max="20" value={formData.procedures} onChange={handleChange} />

          <label>Previous Outpatient Visits:</label>
          <input type="number" name="previous_visits" min="0" max="20" value={formData.previous_visits} onChange={handleChange} />

          <label>Emergency Visits:</label>
          <input type="number" name="emergency_visits" min="0" max="20" value={formData.emergency_visits} onChange={handleChange} />

          <label>Medication Changes:</label>
          <select name="medication_changes" value={formData.medication_changes} onChange={handleChange}>
            <option value="no">No</option>
            <option value="yes">Yes</option>
          </select>

          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
};

export default FormPage;
