from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def list(request):
    context = {}
    return render(request, 'list.html', context)

def content(request):
    context = {}
    return render(request, 'content.html', context)
