FROM python:3.6

ENV PACKAGES "binutils libproj-dev gdal-bin"

RUN apt-get update \
	&& apt-get install -y --no-install-recommends $PACKAGES \
	&& rm -rf /var/lib/apt/lists/*

RUN mkdir /src && cd /src

WORKDIR /src

COPY requirements /src/requirements

RUN pip install -r /src/requirements/dev.txt \
	&& pip install -r /src/requirements/test.txt

COPY scripts /scripts

EXPOSE 8080

ENTRYPOINT [ "/scripts/entrypoint.sh" ]
