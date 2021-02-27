from django.shortcuts import render

# 유저와 권한에 대한 클래스 가져오기 (장고에서 가져오는거라 )
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:  # 비밀번호 확인 값 일치
            user.User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')   # 위에 다 끝내면 아묻따 home 으로
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['uesrname']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:  # 로그인 거부
            return render(request, 'login.html', {'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
   
def logout(reqest):
    if reqest.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(reqest, 'login.html')