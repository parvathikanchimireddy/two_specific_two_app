from django.shortcuts import render

# Create your views here.
def hari(request):
    return render(request,'hari.html')

def parvathi(request):
    return render(request,'parvathi.html')
