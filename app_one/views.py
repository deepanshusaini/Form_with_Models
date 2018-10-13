from django.shortcuts import render
from app_one.forms import Myform

# Create your views here.

def index(request):
    return render(request,'app_one/index.html')

def forms(request):
    form= Myform(request.POST)
    if request.method == 'POST':
        form = Myform(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("Error")
    return render(request,'app_one/form.html',{'form':form})



