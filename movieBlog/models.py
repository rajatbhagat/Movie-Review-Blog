from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField(default='In Progress')
    published_date = models.DateTimeField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserAttributes(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField(default=18)
    phone_number = models.BigIntegerField(blank=True)
    followers = models.IntegerField(default=0)

    def __str__(self):
        resultString = "" + self.user.username
        return resultString


class Comments(models.Model):
    user = models.OneToOneField(User)
    post = models.ForeignKey(Post)
    commenter_name = models.CharField(max_length=100)
    commenter_email = models.EmailField(blank=False)
    comment_text = models.TextField(blank=False)

    def __str__(self):
        resultString = "" + self.user.username + " -> " + self.post.title + " -> " + self.commenter_name
        return resultString