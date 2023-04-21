from django.urls import path

from chatbot.views import slack_events_handler, get_answer


urlpatterns = [
    path("slack/events", slack_events_handler, name="slack_events"),
    path("question", get_answer, name="question")
]
