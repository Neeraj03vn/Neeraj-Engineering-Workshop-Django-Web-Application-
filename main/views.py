from django.shortcuts import render

def firstpage(request):
    return render(request, 'firstpage.html')

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def truss(request):
    return render(request, 'truss.html')
