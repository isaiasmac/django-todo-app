from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Task

@login_required(login_url='login')
def index(request):
	user = get_object_or_404(User, username=request.user.username)
	tasks = Task.objects.filter(user=user)
	return render(request, 'main_app/index.html', {'tasks':tasks})