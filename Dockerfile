FROM python:3.8

ENV APP_HOME=/home/app/jokes

RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . $APP_HOME

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python manage.py makemigrations;python manage.py migrate; python manage.py runserver 0.0.0.0:8080