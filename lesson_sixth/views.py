from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from .models import Human


class List(TemplateView):
    template_name = 'human_list.html'
    def get(self,request):
        all_humans = Human.objects.all()
        the_first_two = Human.objects.all()[:2]
        workers_google = Human.objects.filter(company='google')
        filtered = Human.objects.filter(birth__year=1976)
        ordered = Human.objects.all().order_by('birth')
        sorted = Human.objects.filter(birth__year=1950).order_by('birth')
        sorted_salary = Human.objects.filter(salary__gte=100, salary__lte=3000).order_by('-salary')

        ctx = {
            'all_humans': all_humans,
            'workers_google': workers_google,
            'filtered': filtered,
            'first_two': the_first_two,
            'ordered':ordered,
            'sorted':sorted,
            'sorted_salary': sorted_salary
        }
        return render(request,self.template_name, ctx)

    def post(self, request):
        query = request.POST['search']
        result_list = Human.objects.filter(company=query)
        if result_list.count() != 0:
            context = {
                'result_list': result_list,
                'query': query,
            }
        else:
            context = {
                'empty': "Ничего не найдено",
                'query': query,
            }
        return render(request,'result.html',context)