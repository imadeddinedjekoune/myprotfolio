from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	print(request.user_agent.os)
	print(request.META.get('REMOTE_ADDR'))
	return render(request,"main/test.html")