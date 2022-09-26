FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD [ "streamlit","run","prediction_trial.py","--server.port","5000" ]