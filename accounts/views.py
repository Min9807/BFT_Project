from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

# Create your views here.
# 로그인 부분
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        user_email = request.POST['email'] # 이메일을 입력받는다.
        print(request.POST['email'])
        password = request.POST['password'] # 비번을 입력받는다.
        print(request.POST['password'])
        user = auth.authenticate(request, username=user_email, password=password) # 아이디와 비번을 가져와서 확인한다.
        if user is not None: # 로그인 부분
            print('맞음')
            auth.login(request, user)
            return redirect('main:home') # 아이디 비번 맞으면 다른곳으로 들어감
        else: # 아이디 비번 틀렸을 때
            print('틀림')
            return render(request, 'accounts/signin.html', {'error':'아이디 또는 비밀번호가 틀렸을 때'})
    return render(request, 'accounts/signin.html')

# 로그아웃 부분
def logout(request):
    auth.logout(request)
    return redirect('accounts:signin')


# 회원가입
def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['nickname']).exists():  # 닉네임 중복 체크
            return render(request, 'accounts/signup.html', {'error': '중복된 닉네임 입니다.'})
        elif User.objects.filter(username=request.POST['email']).exists():  # 이메일 중복 체크
            return render(request, 'accounts/signup.html', {'error': '중복된 이메일 입니다.'})
        if request.POST['password'] == request.POST['password_check']: # 비번 같은지 체크
            user = User.objects.create_user( # 새로운 학습자를 만들어서 DB에 저장되는것이다.
                                            last_name=request.POST['last_name'],
                                            username=request.POST['email'],
                                            password=request.POST['password'],
                                            email=request.POST['email'],
                                            department=request.POST['department'],
                                            first_name=request.POST['nickname'])
            user.save()
            return redirect('accounts:signin')
        else:
            return render(request, 'accounts/signup.html', {'error': '비밀번호가 다릅니다.'})
        return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')