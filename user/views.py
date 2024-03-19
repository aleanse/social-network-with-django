from django.shortcuts import render


# Create your views here.

def register(request):

    exemplo = 'TEXTO'

    return render(request,'register.html',context={'exemplo':exemplo})
