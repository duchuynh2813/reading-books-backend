from django.shortcuts import render
from .forms import DangkyForm, DangnhapForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect 

"""class DangkyThanhvien(View):
	def get(sefl,request):
		rF = DangkyForm
		return render(request, 'UserMembers/dangky.html', {'rF':rF})

	def post(self, request):
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

	
		user = User.objects.create_user(username, email, password)
		user.save()
		return HttpResponse('Create user success')"""

def register(request):
    form = DangkyForm()
    if request.method == 'POST':
        form = DangkyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Create user success')
    return render(request, 'UserMembers/dangky.html', {'form': form})

class DangnhapThanhvien(View):
	def get(sefl, request):
		lF = DangnhapForm
		return render(request, 'UserMembers/dangnhap.html', {'lF': lF})

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request,user)
			return HttpResponse('Login user success')
		else:
			return HttpResponse('Login user fail')