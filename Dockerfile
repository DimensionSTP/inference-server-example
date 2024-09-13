FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY app.py ./
COPY data ./data
COPY model ./model
COPY logs ./logs

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]