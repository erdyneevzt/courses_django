from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from .forms import UserCreateForm
from .forms import HumanForm
from lesson_sixth.models import Human
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class MainView(TemplateView):
    template_name = 'ajax.html'
    human_form = HumanForm
    def get(self,request):
        ctx = {}
        ctx['script'] ='alert(5555555);'    # так вызовется скрипт
        if request.user.is_authenticated:
            all_humans = Human.objects.all()
            ctx['humans'] = all_humans
            ctx['human_form'] = self.human_form
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name,{})


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/lesson-eighth/login"
    template_name = "register_8.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView,self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)



class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/lesson-eighth/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)


class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/lesson-eighth/")


def validate_email(request):        # Обработчик JSON запроса от html register_8
    if request.GET:
        email = request.GET.get('email')
        is_taken = User.objects.filter(email=email).exists()
        if is_taken:
            data = {
                 "is_taken": "На этот почтоный ящик уже зарегистрирован пользователь!"
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'ok': "На этот адрес не было регистраций"})

def show_three(request):
    first_three = Human.objects.all()[:3].values()
    context = {
        'elements':list(first_three)
    }
    return JsonResponse(context)

def show_four(request):
    last_four = Human.objects.all()[:4].values()

    context = {
        'elements':list(last_four)
    }
    return JsonResponse(context)

@csrf_exempt        # для корректной работы ajax
def add_human(request):
    if request.POST:
        if request.is_ajax():
            name = request.POST['name']
            surname = request.POST['surname']
            birth = request.POST['birth']
            company = request.POST['company']
            position = request.POST['position']
            language = request.POST['language']
            salary = request.POST['salary']
            human = Human.objects.create(name=name,
                                         surname=surname,
                                         birth=birth,
                                         company=company,
                                         position=position,
                                         language=language,
                                         salary=salary)
            return JsonResponse(human.dict()) # dict метод написанный в самой модели смотри human