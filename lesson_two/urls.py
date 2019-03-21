from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^items$',views.items , name = "items"),
    re_path(r'^items/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})$',views.day_archive , name = "day_archive"),
    re_path(r'^render-template/$', views.render_template),
    re_path(r'^render-template/form-handler/$', views.form_handler),
]