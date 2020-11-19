FROM python:3.8

LABEL maintainer="alanvazquez1999@gmail.com"
LABEL ENV="DEV"
LABEL version="1.0"
LABEL description="This image use the client\
    script to use in conjunction with another \
    server image indacates in the compose file"

ENV PORT=5089

WORKDIR /src
COPY client.py .
COPY test.json .

CMD [ "python", "-u", "client.py" ]
