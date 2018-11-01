# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect, render_to_response   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from guestbook.models import Message, Work, Comment
import datetime
from django.utils.timezone import now
from datetime import datetime
from pytz import timezone
from django.contrib.auth.decorators import login_required
 
@login_required
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
	worklist = []

	# for i in range(Work.objects.count()+1):
	# 	worklist.append(Post.objects.filter(id = i))
	# 	print(worklist[i].name)

	# update db
	# Work.objects.filter(id = 1).update(classification = "IMcamp")
	# Work.objects.filter(id = 2).update(classification = "Web")
	# Work.objects.filter(id = 3).update(classification = "IMcamp")
	# Work.objects.filter(id = 4).update(classification = "Web")
	# for i in range(5,7):
	# 	Work.objects.filter(id = i).update(classification = "IMcmap")
	# for i in range(7,9):
	# 	Work.objects.filter(id = i).update(classification = "Logo")
	# for i in range(9,14):
	# 	Work.objects.filter(id = i).update(classification = "Paintings")
	works = Work.objects.all()
	if "group" in request.GET:
		group_name = request.GET["group"] 
		if group_name == "All":
			works = Work.objects.all()
		else:
			works = Work.objects.filter(classification = group_name)
		# elif "web" in request.GET:
		# 	works = Work.objects.filter(classification = "web")
		# elif "painting" in request.GET:
		# 	works = Work.objects.filter(classification = "paintings")
		# elif "logo" in request.GET:
		# 	works = Work.objects.filter(classification = "logo")
		# elif "others" in request.GET:
		# 	works = Work.objects.filter(classification = "others")
		# else:
		# 	works = Work.objects.all()
	# if "comment_work" in request.GET:
	# 	work_name = request.GET["comment_work"] 
	# 	if group_name == "All":
	# 		works = Work.objects.all()
	# 	else:
	# 		works = Work.objects.filter(classification = group_name)

	return render(request, 'index2.html',locals())

@login_required
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
		talker = request.user
		message = request.POST['message']
		time = datetime.now()     # 擷取現在時間

		Message.objects.create(talker=talker, message=message, time=time)
	# return render_to_response('comments.html',locals())
	return render(request, 'board.html',locals())
@login_required
def comment(request):

	works = Work.objects.all()
	cmts = Comment.objects.all()

	if request.GET: # 某作品的評論頁面
		work = Work.objects.get(id=request.GET["comment_work"])
		cmts = Comment.objects.filter(work__in=request.GET["comment_work"]).all()


	if request.POST:
		if "comment_work" in request.GET: # 某作品的評論頁面
			author = request.user
			comment = request.POST['comment']
			w = Work.objects.get(id=request.GET["comment_work"])
		else: # 所有作品的評論頁面
			author = request.user
			comment = request.POST['comment']
			work = request.POST['choose_work']
			w = Work.objects.get(id=work)

		

		Comment.objects.create(author=author, comment=comment,work = w)
	# return render_to_response('comments.html',locals())
	return render(request, 'comment.html',locals())
