from django.shortcuts import render

# Create your views here.

def index(request):
    work = request.GET.get('work')
    context = {
        'work': work
    }
    return render(request, 'tempapp/index.html' , context)

def create_todo(request):
    return render(request, 'tempapp/create_todo.html')

def detail(request,work):
    context = {
        'work' : work
    }
    return render(request, 'tempapp/detail.html', context)
