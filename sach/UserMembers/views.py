from django.shortcuts import render
from .forms import DangkyForm, DangnhapForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json


class DangkyThanhvien(View):
    def get(self, request):
        rF = DangkyForm
        return render(request, 'UserMembers/dangky.html', {'rF': rF})

    def post(self, request):
       # body = request.body.decode('utf-8')
       # jsonbody = json.loads(body)

        #print(jsonbody)

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse("Dang ky thanh cong")
        # return HttpResponse('Login user success')


class DangnhapThanhvien(View):
    def get(self, request):
        lF = DangnhapForm
        return render(request, 'UserMembers/dangnhap.html', {'lF': lF})

    def post(self, request):
        """body = request.body.decode('utf-8')
        jsonbody = json.loads(body)"""

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            """login(request, user)"""
            return HttpResponse( 'Đăng nhập không thành công, user không tồn tại')
        
        login(request, user)
        return HttpResponse( 'Đăng nhập thành công user: %s ' %user.id)

class ViewUser(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('Bạn vui lòng đăng nhập')
        else:
            return HttpResponse('<h1> Đây là View User </h1>')