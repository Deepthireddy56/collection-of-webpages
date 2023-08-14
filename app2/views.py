from django.shortcuts import render

# Create your views here
def document(request):
    return render(request,'document.html')
def facebook(request):
    return render(request,'facebook.html')
def table1(request):
    return render(request,'table1.html')
def table2(request):
    return render(request,'table2.html')
def amazon(request):
    return render(request,'amazon.html')