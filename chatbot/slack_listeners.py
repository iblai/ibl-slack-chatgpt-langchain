import logging
import os
import requests

from slack_bolt import App

logger = logging.getLogger(__name__)

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
    # disable eagerly verifying the given SLACK_BOT_TOKEN value
    token_verification_enabled=False,
)


@app.event("app_mention")
def handle_app_mentions(logger, event, say):
    logger.info(event)
    say(f"Hi there, <@{event['user']}>")

@app.event("message")
def event_test(body, say, logger):
    logger.info(body)
    message = body["event"]["text"]
    response = requests.post("http://api.mentor.ibl.ai/ask/", json={"question": message, "database": "default", "with_sources": "true"})
    body = response.json()
    say(body["answer"])