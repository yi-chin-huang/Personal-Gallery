from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
	imagelist = [["cover.png","portfolio-wrapper1"], 
	["impossible website.png","portfolio-wrapper2"], 
	["傳單.png","portfolio-wrapper1"], 
	["prolog.png","portfolio-wrapper2"],
	["營服白.png","portfolio-wrapper1"],
	["營服.png","portfolio-wrapper1"],
	["路跑.png","portfolio-wrapper1"],
	["chimeiclothes.png","portfolio-wrapper1"],
	["painting1.jpg","portfolio-wrapper1"],
	["painting2.jpg","portfolio-wrapper1"],
	["painting3.jpg","portfolio-wrapper1"],
	["painting4.jpg","portfolio-wrapper1"],
	["painting.jpg","portfolio-wrapper1"]]

	return render(request, 'index2.html',locals())
