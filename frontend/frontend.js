const body = {
  age: selectedAge,
  total_visits: parseInt(totalVisits, 10),
  diagnoses: selectedDiagnosesArray, // array of strings length <= 3
  glucose_test: parseFloat(glucoseValue),
  a1c_test: parseFloat(a1cValue)
}

const res = await fetch("http://localhost:8000/submit", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify(body)
});
const data = await res.json();
console.log("Prediction:", data);
