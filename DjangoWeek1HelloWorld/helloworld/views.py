# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect, render_to_response   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import Message, Work, Comment
import datetime
from django.utils.timezone import now
from datetime import datetime
from pytz import timezone

def index(request):
	# imagelist = [["cover.png","portfolio-wrapper1"], 
	# ["impossible website.png","portfolio-wrapper2"], 
	# ["傳單.png","portfolio-wrapper1"], 
	# ["prolog.png","portfolio-wrapper2"],
	# ["營服白.png","portfolio-wrapper1"],
	# ["營服.png","portfolio-wrapper1"],
	# ["路跑.png","portfolio-wrapper1"],
	# ["chimeiclothes.png","portfolio-wrapper1"],
	# ["painting1.jpg","portfolio-wrapper1"],
	# ["painting2.jpg","portfolio-wrapper1"],
	# ["painting3.jpg","portfolio-wrapper1"],
	# ["painting4.jpg","portfolio-wrapper1"],
	# ["painting.jpg","portfolio-wrapper1"]]
	path = request.path 
	
	works = Work.objects.all()
	cmts = Comment.objects.all()
    # return render_to_response('menu.html',locals())
	return render(request, 'index2.html',locals())

def board(request):
	# path = request.path 
	# host=request.get_host()
	# fp=request.get_full_path()
	# sec = request.is_secure()


	# t1 = Message.objects.create(talker='Yi Chin', message='Hello, Doggo!' )
	# t2 = Message.objects.create(talker='Golden', message='Woof!' )
	# t3 = Message.objects.create(talker='Shiba', message='Woof Woof!')

	
	# Message.objects.filter(talker="Shiba").delete()
	# Message.objects.filter(talker="Yi Chin").delete()
	# Message.objects.filter(talker="Golden").delete()
	msgs = Message.objects.all()


	if request.POST:
		talker = request.POST['talker']
		message = request.POST['message']
		time = datetime.now()     # 擷取現在時間

		Message.objects.create(talker=talker, message=message, time=time)
	# return render_to_response('comments.html',locals())
	return render(request, 'board.html',locals())

def comment(request):

	works = Work.objects.all()
	cmts = Comment.objects.all()

	if request.POST:
		author = request.POST['author']
		comment = request.POST['comment']
		work = request.POST['choose_work']
		w = Work.objects.get(id=work)

		Comment.objects.create(author=author, comment=comment,work = w)
	# return render_to_response('comments.html',locals())
	return render(request, 'comment.html',locals())
