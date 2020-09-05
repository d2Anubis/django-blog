from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from articles.models import Article,Category

# Create your views here.
def sign(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:articles')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', { 'form': form })

def about(request):
    return render(request,'users/about.html')

def logging_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form': form })

def logging_out(request):
        logout(request)
        return redirect('home')


def topic(request,sub):
    page_obj = Article.objects.filter(category=sub)
    return render(request,'articles/articlespage.html',{'page_obj':page_obj})