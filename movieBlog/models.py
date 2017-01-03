from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.OneToOneField(User)
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField(default='In Progress')
    published_date = models.DateTimeField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title