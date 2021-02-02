FROM ubuntu:latest

RUN mkdir -p /model
WORKDIR /model

COPY Model.sav .
COPY main.py .
COPY requirements.txt .

RUN apt update && \
    apt upgrade -y

RUN apt install -y python3 && \
    apt install -y python3-pip && \
    pip3 install -r requirements.txt

CMD [ "python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--debug", "--workers", "3" ]
