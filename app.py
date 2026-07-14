from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    input_data = pd.DataFrame({
        "N":[N],
        "P":[P],
        "K":[K],
        "temperature":[temperature],
        "humidity":[humidity],
        "ph":[ph],
        "rainfall":[rainfall]
    })

    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000)),
    debug=False
    )