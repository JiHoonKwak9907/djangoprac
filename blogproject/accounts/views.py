from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User # 장고가 이미 가지고 있는 User테이블

def login(request):
  # POST요청이 들어오면 로그인 처리를 해줌
  if request.method =='POST':
    userid = request.POST['username']
    pwd = request.POST['password']
    user = auth.authenticate(request, username=userid, password=pwd)
    if user is not None:
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, 'login.html')
  # GET요청이 들어오면 login form을 담고있는 login.html을 뛰워주는 역할을 함
  else:
      return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('home')