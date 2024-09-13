from collections import OrderedDict

import pandas as pd
import joblib
import json

from flask import Flask, Response


app = Flask(__name__)

import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
)

data_dir = "./data"
data = pd.read_csv(f"{data_dir}/iris_with_category_index.csv")
model_dir = "./model"
model = joblib.load(f"{model_dir}/iris_model.pkl")


@app.route("/predict/<int:data_id>", methods=["GET"])
def predict(data_id):
    logging.info(f"Received prediction request for data_id: {data_id}")

    if data_id not in data.index:
        error_response = json.dumps(OrderedDict([("error", "Data not found")]))
        return Response(
            error_response,
            status=404,
            mimetype="application/json",
        )

    input_data = data.iloc[data_id].drop("class").values.reshape(1, -1)
    prediction = model.predict(input_data)

    response = json.dumps(
        OrderedDict(
            [
                ("data_id", data_id),
                ("class", int(prediction[0])),
            ]
        )
    )

    return Response(
        response,
        status=200,
        mimetype="application/json",
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
    )
