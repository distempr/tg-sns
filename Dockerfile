FROM python:3.12-slim

RUN set -ex; \
      apt-get update; \
      apt-get install -y zip; \
      rm -rf /var/lib/apt/lists/* 

RUN mkdir /usr/lib/lambda

WORKDIR /usr/lib/lambda

COPY requirements.txt .

RUN set -ex; \
      pip install --no-cache-dir --target ./package -r requirements.txt; \
      cd package; \
      zip -r /usr/lib/lambda/tg-sns.zip .

COPY lambda_function.py .
RUN zip /usr/lib/lambda/tg-sns.zip lambda_function.py

CMD ["cp", "/usr/lib/lambda/tg-sns.zip", "/mnt/"]
