# app.py (Flask backend)
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load saved model
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # JSON from frontend
    features = np.array(data["features"]).reshape(1, -1)

    prediction = model.predict(features)[0]

    return jsonify({"prediction": str(prediction)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
