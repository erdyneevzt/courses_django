from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainView.as_view()),
    url(r'^register$', views.RegisterFormView.as_view()),
    url(r'^login$', views.LoginFormView.as_view()),
    url(r'^logout$', views.LogoutView.as_view()),
    url(r'^validate-email', views.validate_email),
    url(r'^show-three',views.show_three),
    url(r'^show-four',views.show_four),
    url(r'^add-human',views.add_human),
]