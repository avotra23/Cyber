from django.shortcuts import render

# Create your views here.

def index(request):
    data = "Nom"
    return render(request,'Fact/index.html',context={'donner': data})