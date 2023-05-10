from django.shortcuts import  render, redirect

from .forms import SignUpForm

from django.contrib.auth import login

from django.contrib import messages

def sign_up_view(request):
	"""The sign_up request"""
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Sign Up successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful Sign Up. Invalid information.")
	form = SignUpForm()
	return render (request=request, template_name="account/templates/sign_up.html", context={"sign_up_form":form})



# Create your views here.
