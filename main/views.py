from django.shortcuts import render
from django.http import HttpResponse
from .models import Visitors , Emails


def index(request):
	v = Visitors()
	v.ip = request.META.get('REMOTE_ADDR')
	v.info = request.user_agent.os
	v.save()

	if request.method == 'POST':
		e = Emails()
		e.send_name = request.POST['user_name']
		e.send_email = request.POST['user_email']
		e.send_context = request.POST['user_project']
		e.save()
	return render(request,"main/index.html")