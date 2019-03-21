from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
# def view(request):
#     list =[0,232,45,123,4,53423,54,23]
#     template = loader.get_template('index.html')
#     context = {
#         "test": "TEXT!",
#         "list": list,
#         "name": "Alex",
#         "surname": "Jazun",
#         "coords": {
#             "x": "x coords",
#             "y": "y coords",
#         },
#         'list':[1,2,3,4]
#     }
#     return HttpResponse(template.render(context, request))

def view(request):
    list = [0, 232, 45, 123, 4, 53423, 54, 23]
    context = {
        "test": "TEXT!",
        "list": list,
        "name": "Alex",
        "surname": "Jazun",
        "coords": {
            "x": "x coords",
            "y": "y coords",
        },
        #'list': [1, 2, 3, 4]
    }
    return render(request, "index.html", context)