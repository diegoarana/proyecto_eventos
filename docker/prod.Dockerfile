FROM python:3.6

ENV PACKAGES "binutils libproj-dev gdal-bin"

RUN apt-get update \
	&& apt-get install -y --no-install-recommends $PACKAGES \
	&& rm -rf /var/lib/apt/lists/*

RUN mkdir /src && cd /src

WORKDIR /src

COPY project /src

COPY requirements /src/requirements

RUN pip install -r /src/requirements/production.txt

EXPOSE 8080

CMD python manage.py makemigrations \
  && python manage.py migrate \
  && python manage.py runserver 0.0.0.0:8080
