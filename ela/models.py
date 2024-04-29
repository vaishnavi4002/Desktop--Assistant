from django.db import models
from django.contrib.auth.models import User

class QueryHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.query_text}'