from django.shortcuts import render

def homepage(request):
    return render(request,'taskapp/home.html')

def aboutpage(request):
    return render(request,'taskapp/about.html')

def parkingpage(request):
    return render(request,'taskapp/parking.html')

def servicepage(request):
    return render(request,'taskapp/service.html')

def fastagpage(request):
    return render(request,'taskapp/fastag.html')

def careerpage(request):
    return render(request,'taskapp/career.html')

def contactpage(request):
    return render(request,'taskapp/contact.html')

