FROM python:3.6

RUN useradd -u 777 -r -m -U app
RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
