from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize app
app = Flask(__name__)

# Load your trained pipeline
model = joblib.load("churn_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON input
        data = request.get_json()

        # Convert to DataFrame (model expects same feature names as training)
        df = pd.DataFrame([data])

        # Make predictions
        pred = model.predict(df)[0]
        proba = model.predict_proba(df)[0, 1]

        # Return JSON response
        return jsonify({
            "prediction": int(pred),              # 0 = stay, 1 = churn
            "churn_probability": float(proba)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
