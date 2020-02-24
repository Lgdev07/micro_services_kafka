FROM python:3.8.0
RUN mkdir -p /kafka_code
WORKDIR /kafka_code
ADD ./requirements.txt /kafka_code/requirements.txt
RUN pip install -r requirements.txt
COPY . /kafka_code
