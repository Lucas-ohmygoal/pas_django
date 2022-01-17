from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pas.models import PasUser


def toLogin_view(request):
    return render(request, 'login.html')

def toIndex_view(request):
    id = request.POST.get('userName','')
    password = request.POST.get('passWord','')

    if id and password:
        c = PasUser.objects.filter(user_id=id, user_pwd = password).count()
        if c==1:
            return HttpResponse('Successfully login!!!')
        else:
            return HttpResponse('Did you forget your password?')
    else:
        return HttpResponse('Fail to login!!!')

def login_view(request):
    return render(request, 'login.html')

def toRegister_view(request):
    return render(request, 'register.html')

def register_view(request):
    return render(request, 'register.html')

def stuInfo_view(request):
    return render(request, 'login.html')

def score_view(request):
    return render(request, 'login.html')

def addInfo_view(request):
    return render(request, 'login.html')