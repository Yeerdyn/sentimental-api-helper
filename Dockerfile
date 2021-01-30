FROM python:3.8
WORKDIR /app
COPY src/requirements.txt ./
RUN pip install -r requirements.txt
COPY src /app

RUN python -m dostoevsky download fasttext-social-network-model
RUN python -m dostoevsky download fasttext-toxic-model

EXPOSE 80
CMD ["python", "app.py"]