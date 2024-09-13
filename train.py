import os

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


def train():
    data_dir = "./data"
    data = pd.read_csv(f"{data_dir}/iris_with_category_index.csv")

    x = data.drop(columns=["class"])
    y = data["class"]
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=2024,
    )

    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    model_dir = "./model"
    if not os.path.exists(model_dir):
        os.makedirs(
            model_dir,
            exist_ok=True,
        )

    joblib.dump(
        model,
        f"{model_dir}/iris_model.pkl",
    )
    print("model file saved.")

    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)

    log_dir = "./logs"
    if not os.path.exists(log_dir):
        os.makedirs(
            log_dir,
            exist_ok=True,
        )

    with open(f"{log_dir}/model_performance.log", "w") as f:
        f.write(f"Train Accuracy: {train_accuracy:.4f}\n")
        f.write(f"Test Accuracy: {test_accuracy:.4f}\n")

        f.write("\nTrain Classification Report:\n")
        f.write(classification_report(y_train, y_train_pred))

        f.write("\nTest Classification Report:\n")
        f.write(classification_report(y_test, y_test_pred))
    print("model report saved.")


if __name__ == "__main__":
    train()
