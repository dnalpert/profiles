from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import profile
from .forms import profileForm

# Create your views here.
def index(request):
    context = {'profile':profile.objects.all()}
    template = 'index.html'
    return render(request, template, context)

@login_required(login_url='http://127.0.0.01:8000/account/login')
def UserProfile(request, username):

    user_url = User.objects.get(username=username)

    context = {'user_url': user_url}
    template = 'account/profile.html'
    return render(request, template, context)

@login_required(login_url='http://127.0.0.01:8000/account/login')
def EditUserProfile(request):
    user = request.user
    if request.method == 'POST':
        form = profileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=user.username)
    else:
        user = request.user
        user_profile = user.profile
        form = profileForm(instance=user_profile)


    context = {'user':user, 'form': form}
    template = 'account/edit_profile.html'
    return render(request, template, context)

