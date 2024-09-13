# Inference Server Example

This project demonstrates a simple inference server using Flask, Docker, and a pre-trained machine learning model based on the Iris dataset. The server provides an API to predict the category of an Iris plant based on its features.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Model Training](#model-training)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Logs](#logs)
- [Troubleshooting](#troubleshooting)

## Requirements

To run this project, you need to have the following installed:

- Docker
- Docker Compose

If Docker is not installed, follow these steps:

### Docker Installation (Ubuntu 22.04 LTS)

1. Update your package list:

    ```bash
    sudo apt-get update
    ```

2. Install required dependencies:
    ```bash
    sudo apt-get install ca-certificates curl gnupg lsb-release
    ```

3. Add Docker’s official GPG key:
    ```bash
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    ```

4. Set up the Docker stable repository:
    ```bash
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

5. Install Docker:
    ```bash
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

6. Start Docker:
    ```bash
    sudo systemctl start docker
    sudo systemctl enable docker
    ```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/inference-server-example.git
    cd inference-server-example
    ```

2. Install required Python packages (if you are running locally):
    ```bash
    pip install -r requirements.txt
    ```

## Model Training

Before running the server, you need to train the model and save the trained model as a .pkl file. Run the following command to execute train.py and generate the model file:

```bash
python train.py
```

This will generate a file named iris_model.pkl model directory in the project.

## Usage

Once the model is trained and the server is running, you can interact with the API.

### Docker Compose

If you want to run the server inside Docker, use the following command to build and run the Docker container:

```bash
docker-compose up --build
```

The API will be accessible at http://localhost:5000.

### Example Request

To get a prediction for the Iris dataset, send a GET request:

```bash
curl http://localhost:5000/predict/1
```

### Example Response

```json
{
  "data_id": 1,
  "class": 0
}
```

If you request an invalid data_id, the server will return a 404 error:

```bash
curl http://localhost:5000/predict/9999
```

Response:

```json
{
  "error": "Data not found"
}
```

## API Documentation

### 1. Prediction Endpoint

- URL: /predict/<data_id>
- Method: GET
- Parameters:
    - data_id (integer): The ID of the data entry from the Iris dataset to predict.
- Response:
    - Success: 200 OK with a JSON body containing:
        - data_id: The ID of the input data.
        - class: The predicted category (classification).
    - Failure: 404 Not Found if the data_id is invalid or does not exist.

Example:

```bash
GET /predict/1
```

```json
{
  "data_id": 1,
  "class": 0
}
```

## Logs

Logs are stored in the logs directory and can be accessed both from inside and outside the Docker container.

- The main log file is located at logs/app.log.
- You can inspect logs using:

    ```bash
    cat logs/app.log
    ```

## Troubleshooting

- If the container fails to start, check the logs using:

    ```bash
    docker-compose logs
    ```

- If you need to stop the container:

    ```bash
    docker-compose down
    ```

If you encounter any issues or need further help, please open an issue in the repository.
