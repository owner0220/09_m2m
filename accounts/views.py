from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

from .forms import UserCustomCreationForm

# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
@login_required    
def user_list(request):
    User = get_user_model()
    user = User.objects.all()
    return render(request,"accounts/user_list.html",{"Tuser":user})

@login_required
def user_detail(request,user_pk):
    User = get_user_model()
    user = get_object_or_404(User,id=user_pk)
    return render(request,"accounts/user_detail.html",{'Tuser':user})

@login_required
def followings(request,user_pk):
    User = get_user_model()
    user = get_object_or_404(User,id=user_pk)
    return render(request,'accounts/user_followings.html',{'Tuser':user})    
    
@login_required
def followers(request,user_pk):
    User = get_user_model()
    user = get_object_or_404(User,id=user_pk)
    return render(request,'accounts/user_followers.html',{'Tuser':user})    

@login_required
def follow(request,user_pk):
    User = get_user_model()
    me = request.user
    you = get_object_or_404(User,id=user_pk)
    if me != you:
        if you in me.followings.all():
            me.followings.remove(you)
        else:
            me.followings.add(you)
    return redirect('accounts:user_detail',user_pk)
    