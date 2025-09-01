from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load trained model
arima_model = joblib.load("arima_model.pkl")

app = Flask(__name__)

@app.route("/forecast", methods=["POST"])
def forecast():
    try:
        data = request.get_json()
        steps = int(data.get("steps", 5))  # default 5 years

        # forecast = arima_model.forecast(steps=steps)
        forecast = arima_model.predict(steps)
        forecast = forecast.tolist()

        return jsonify({"forecast": forecast})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
