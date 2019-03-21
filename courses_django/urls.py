"""courses_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
#from lesson_two import views

urlpatterns = [
    #path(r'',include('lesson_one.urls')),
    path('admin/', admin.site.urls),
    #path(r'',views.home)
    #path(r'',include('lesson_two.urls')),
    url(r'^', include('lesson_two.urls')),
    url(r'^lesson-third/', include('lesson_third.urls')),
    url(r'^lesson-fifth/', include('lesson_fifth.urls')),
    url(r'^lesson-sixth/',include('lesson_sixth.urls')),
    url(r'^lesson-seventh/',include('lesson_seventh.urls')),
    url(r'^lesson-eighth/',include('lesson_eighth.urls')),
    #url(r'^admin/',admin.site.urls),
]
