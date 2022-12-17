FROM python:3.10.2

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "main.py"]