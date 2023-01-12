FROM python:3.9

WORKDIR /app

COPY treq.txt /app/

RUN pip3 install -r treq.txt

COPY . /app

CMD python3 Translater.py
