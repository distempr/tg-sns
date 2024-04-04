FROM python:3.12-slim

RUN set -ex; \
      mkdir /usr/lib/lambda /var/lib/lambda /var/lib/lambda/host

RUN set -ex; \
      apt-get update; \
      apt-get install -y zip; \
      rm -rf /var/lib/apt/lists/* 

WORKDIR /usr/lib/lambda

COPY requirements.txt .

RUN set -ex; \
      pip install --no-cache-dir --target ./package -r requirements.txt; \
      cd package; \
      zip -r /var/lib/lambda/tg-sns-lambda.zip .

COPY lambda_function.py .
RUN zip /var/lib/lambda/tg-sns-lambda.zip lambda_function.py

CMD ["cp", "/var/lib/lambda/tg-sns-lambda.zip", "/var/lib/lambda/host/"]
