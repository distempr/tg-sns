import re

import boto3
import requests


ssm = boto3.client("ssm")


# Adapted from python-telegram-bot package
# https://github.com/python-telegram-bot/python-telegram-bot/blob/master/telegram/helpers.py
def escape_markdown(text):
    escape_chars = r"\_*[]()~`>#+-=|{}.!"
    return re.sub(f"([{re.escape(escape_chars)}])", r"\\\1", text)


def lambda_handler(event, context):
#    print(event)

    chat = ssm.get_parameter(
        Name="/tg-sns/chat",
        WithDecryption=False
    )["Parameter"]["Value"]
    chat = int(chat)

    token = ssm.get_parameter(
        Name="/tg-sns/token",
        WithDecryption=True
    )["Parameter"]["Value"]

    subject = event["Records"][0]["Sns"]["Subject"]

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data={
            "chat_id": chat,
            "parse_mode": "MarkdownV2",
            "text": f"*distempr SNS:* {escape_markdown(subject)}"
        }
    )
