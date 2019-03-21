from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.base import View
from lesson_sixth.models import Human
from .forms import UserCreateForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect

# Create your views here.
class MainView(TemplateView):
    template_name = 'main_seventh.html'

    def get(self,request):
        if request.user.is_authenticated:
            humans = Human.objects.all()
            ctx = {}
            ctx['humans'] = humans
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name,{})


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/lesson-seventh/login"
    template_name =  "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView,self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/lesson-seventh/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/lesson-seventh/")