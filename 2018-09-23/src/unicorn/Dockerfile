FROM python:3.6

RUN apt-get update
RUN apt-get install -y python-pip

RUN mkdir -p /var/www/sample
WORKDIR /var/www/sample/

COPY requirements.txt /var/www/sample/
RUN pip install -r requirements.txt

CMD ["gunicorn", "app:app"]
