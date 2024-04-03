FROM python:3.12-slim

RUN set -ex; \
      mkdir /usr/lib/lambda /var/lib/lambda

RUN set -ex; \
      apt-get update; \
      apt-get install -y zip; \
      rm -rf /var/lib/apt/lists/* 

WORKDIR /usr/lib/lambda

COPY requirements.txt .

RUN set -ex; \
      pip install --no-cache-dir --upgrade pip; \
      pip install --no-cache-dir --target ./package -r requirements.txt

COPY build-lambda-package /usr/bin/build
COPY lambda_function.py .

CMD ["/usr/bin/build"]
