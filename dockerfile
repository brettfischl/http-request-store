FROM python:3.6

RUN useradd -u 777 -r -m -U app
RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN export FLASK_APP=/app/app.py

CMD ["python", "app.py"]
