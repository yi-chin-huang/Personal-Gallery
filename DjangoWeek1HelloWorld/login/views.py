from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import template
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def welcome(request):
	return render_to_response('welcome.html',locals())


def login(request):
	if request.user.is_authenticated: 
		return HttpResponseRedirect('/welcome/')

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if  user is not None and user.is_active:
		auth.login(request, user) #maintain the state of login
		return HttpResponseRedirect('/welcome/',locals())
	else:
		return render_to_response('login.html',locals())

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/welcome/',locals())


def signup(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		try:
			user = User.objects.get(username=username)
		except:
			user = None
		if user is not None:
			message = '此使用者已經有人使用'
		else:
			user = User.objects.create_user(username = username, password = password)
			user.save()
			message = "註冊成功"
			return render(request, "welcome.html", locals())
	return render(request, 'signup.html', locals())
