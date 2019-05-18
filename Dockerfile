FROM python:3.6.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev --no-install-recommends \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./code /code/

CMD python manage.py runserver 0.0.0.0:$PORT