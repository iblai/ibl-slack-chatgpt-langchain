import logging
import os
from dotenv import load_dotenv
import requests
from iblGpt.settings import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET

from slack_bolt import App

load_dotenv()

logger = logging.getLogger(__name__)

app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET,
    # disable eagerly verifying the given SLACK_BOT_TOKEN value
    token_verification_enabled=False,
)


@app.event("app_mention")
def handle_app_mentions(logger, event, say):
    logger.info(event)
    say(f"Hi there, <@{event['user']}>")


@app.event("message")
def event_message(body, say, logger):
    logger.info(body)
    message = body["event"]["text"]
    response = requests.post(
        "http://api.mentor.ibl.ai/ask/",
        json={"question": message, "database": "default", "with_sources": "true"},
    )
    body = response.json()
    say(body["answer"])
