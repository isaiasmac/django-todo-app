from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm

def my_login(request):
	if request.user.is_authenticated:
		return redirect(reverse('main_index'))
		
	if request.method == "POST":
		form = LoginForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user = authenticate(request, username=username, password=password)
			
			if user is not None:
				print("User is logged")
				login(request, user)
				return redirect(reverse('main_index'))
			else:
				messages.add_message(request, messages.ERROR, "Usuario o contraseña invalidos")
				return redirect(reverse('my_login'))
		else:
			return render(request, 'user_app/login.html', {'form': form})
			# print("FORM is not valid")
			# errors = form.errors
			# print(errors)
			# messages.add_message(request, messages.ERROR, errors)
			# return redirect(reverse('login'))
	else:
		form = LoginForm()
		return render(request, 'user_app/login.html', {'form': form})

def my_logout(request):
	logout(request)
	messages.add_message(request, messages.INFO, "Has cerrado sesión correctamente.")
	return redirect(reverse('my_login'))
