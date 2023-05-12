from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import CreateUserForm, ChangePasswordForm, NewsPostForm
from .models import NewPost, Profile


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    user = request.user
    posts = NewPost.objects.all()

    context = {
        'user': user,
        'posts': posts
    }

    return render(request, 'home.html', context)


@login_required()
def profile(request):
    posts = NewPost.objects.filter(author=request.user)
    post_count = posts.count()
    context = {'post_count': post_count}

    return render(request, 'profile.html', context)


@login_required()
def password_change(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ChangePasswordForm(user=request.user)

    context = {'form': form}

    return render(request, 'password_change.html', context)


def create_news(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()



            return redirect('home')
    else:
        form = NewsPostForm()

    context = {'form': form}

    return render(request, 'create_news.html', context)

