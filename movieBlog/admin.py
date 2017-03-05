from django.contrib import admin
from movieBlog.models import Post, Comments, UserAttributes

# Register your models here.

admin.site.register(UserAttributes)
admin.site.register(Post)
admin.site.register(Comments)