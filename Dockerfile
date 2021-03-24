FROM gcr.io/google-appengine/python

RUN virtualenv /env -p python3.7

RUN apt-get update
RUN apt-get -qq -y install libzbar0

ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

ADD . /app

ENV PORT 8080

CMD gunicorn -b :$PORT app:app