from django.shortcuts import render

# Create your views here.
def animation1(request):
    return render(request,'animation1.html')
def animation2(request):
    return render(request,'animation2.html')
def application(request):
    return render(request,'application.html')
def card(request):
    return render(request,'card.html')
def testing(request):
    return render(request,'testing.html')