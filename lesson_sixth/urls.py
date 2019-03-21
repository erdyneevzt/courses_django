from django.conf.urls import url
from .views import List

urlpatterns = [
    url(r'^$', List.as_view(), name='list-view'),
]