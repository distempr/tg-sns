# tg-sns

Holds the code for a Lambda that sends SNS notifications through to a Telegram bot. Uses Docker to build the function zip archive.

## Install

- Create Lambda and subscribe it to an SNS topic.
  - Runtime: Python 3.12
  - Exec role permissions:
    - SSM: GetParameter(s) on /tg-sns/*
- Create S3 bucket in which the function zip file will be published.
- Create SSM parameters:
  - `/tg-sns/chat` (String): chat ID that notifcations will be sent to.
  - `/tg-sns/token` (SecureString): bot token.
- Edit variables in `deploy` if necessary.
- `./deploy`
