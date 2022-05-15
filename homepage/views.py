from django.shortcuts import render

# Create your views here.

# 主页
def index(req):
    return render(req, 'index.html')

# 个人信息
def user_profile(req):
    return render(req, 'user-profile.html')

def login(req):
    return render(req, 'authentication-signin.html')