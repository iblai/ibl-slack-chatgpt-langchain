from django.urls import path

from views import slack_events_handler


urlpatterns = [
    path("slack/events", slack_events_handler, name="slack_events"),
]