from django.db import models
from chatbot.utils import count_tokens


class MessageClient(models.Model):
    conversation_id = models.TextField()

    def get_history(self, max_token=400):
        history = ""
        start = "Here is our chat history. We were talking about the things below:\n"
        for m in self.messages.all():
            parsed = f"Question: {m.question}\nAnswer: {m.answer}\n\n"
            if count_tokens(parsed + start) > max_token:
                break
            history += parsed
        if history:
            history = start + history
        return history


class MessageEntry(models.Model):
    question = models.TextField()
    answer = models.TextField()
    answered_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(
        MessageClient, on_delete=models.CASCADE, related_name="messages"
    )
