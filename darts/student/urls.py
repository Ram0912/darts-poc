from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<id>[\d]+)/$', StudentViewSet.as_view()),
    url(r'^total/$', StudentTotalViewSet.as_view()),
    url(r'^subject/average/$', SubjectAverageViewSet.as_view()),
    url(r'^total/cache$', GetCacheDf.as_view()),
]