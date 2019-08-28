FROM python:3.6

WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . .

EXPOSE 8000

CMD make run
