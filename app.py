from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("crop_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        n = float(request.form["nitrogen"])
        p = float(request.form["phosphorus"])
        k = float(request.form["potassium"])
        ph = float(request.form["ph"])

        input_data = pd.DataFrame([[n, p, k, ph]], columns=["N", "P", "K", "pH"])

        prediction = model.predict(input_data)[0]
        confidence = round(max(model.predict_proba(input_data)[0]) * 100, 1)

        return render_template(
            "index.html",
            result=prediction,
            confidence=confidence,   # <-- this line was missing
            values={"nitrogen": n, "phosphorus": p, "potassium": k, "ph": ph},
        )
    except ValueError:
        return render_template("index.html", error="Please enter valid numbers.")


if __name__ == "__main__":
    app.run(debug=True)