from django.shortcuts import render

# Create your views here.

# 메인화면
def home(request):
    return render(request, 'main/main.html')