import re

import boto3
import requests


SSM_PARAM_NS = "tg-sns"
TG_BASE_URL = "https://api.telegram.org"


ssm = boto3.client("ssm")


# Adapted from python-telegram-bot package
# https://github.com/python-telegram-bot/python-telegram-bot/blob/master/telegram/helpers.py
def escape_markdown(text):
    escape_chars = r"\_*[]()~`>#+-=|{}.!"
    return re.sub(f"([{re.escape(escape_chars)}])", r"\\\1", text)


def get_parameter(name, decrypt=False):
    return ssm.get_parameter(
        Name=f"/{SSM_PARAM_NS}/{name}",
        WithDecryption=decrypt
    )["Parameter"]["Value"]


def lambda_handler(event, context):
    chat = get_parameter("chat")
    token = get_parameter("token", decrypt=True)

    for record in event["Records"]:
        if "Sns" not in record:
            continue

        if record["Sns"]["Type"] != "Notification":
            continue

        topic = record["Sns"]["TopicArn"].split(":")[-1]
        subject = record["Sns"]["Subject"]

        requests.post(
            f"{TG_BASE_URL}/bot{token}/sendMessage",
            data={
                "chat_id": chat,
                "parse_mode": "MarkdownV2",
                "text": f"*{escape_markdown(topic)} SNS:* {escape_markdown(subject)}"
            }
        )
