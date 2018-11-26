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
import urllib
 
# @login_required
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
	works = Work.objects.all().order_by('id')
	
	if "group" in request.GET:
		group_name = request.GET["group"] 
		if group_name == "All":
			works = Work.objects.all().order_by('id')
		else:
			works = Work.objects.filter(classification = group_name).order_by('id')

	return render(request, 'index2.html',locals())

# @login_required
def board(request):

	msgs = Message.objects.all().order_by('id')
	
	# for m in msgs:
	# 	m.time =  m.time.strftime("%Y-%m-%d %H:%M:%S")

	if "sendmsg" in request.POST:
		talker = request.user
		message = request.POST['message']
		time = datetime.now()     # 擷取現在時間

		Message.objects.create(talker=talker, message=message, time=time)
		return render(request, 'board.html',locals())

	if "delmsg" in request.POST:
		mid = request.POST['msgid']
		Message.objects.filter(id = mid).delete()
		return render(request, 'board.html',locals())

	if "edit" in request.POST:
		mid = request.POST['edit_msgid']
		return redirect('edit', mid = mid)
		
	if "searchmsg" in request.POST:
		search_content = request.POST['search_content']
		msgs = Message.objects.filter(message__contains = search_content)
	
	if "finish_search" in request.POST:
		msgs = Message.objects.all().order_by('id')


	return render(request, 'board.html',locals())

# @login_required
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

		

		Comment.objects.create(author = author, comment = comment, work = w)
	# return render_to_response('comments.html',locals())
	return render(request, 'comment.html',locals())


def edit(request,mid):
	if "edit_msg" in request.POST:
		new_msg = request.POST['edit_content']
		Message.objects.filter(id = mid).update(message = new_msg)
		return HttpResponseRedirect('/board/',locals())
	return render(request, 'edit.html', locals())

