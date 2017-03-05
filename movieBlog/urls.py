from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.get_all_posts, name='posts'),
]