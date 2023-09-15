from django.shortcuts import render
from django.http import HttpResponse
from .models import Visitors


def index(request):
	v = Visitors()
	v.ip = request.META.get('REMOTE_ADDR')
	v.info = request.user_agent.os
	v.save()

	return render(request,"main/index.html")