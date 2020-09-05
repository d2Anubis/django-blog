from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Article
from . import forms

# Create your views here.
def home(request):
    articles = Article.objects.all().order_by('-date')[:3]
    return render(request,'articles/homepage.html',{'articles':articles})


def articles(request):
    articles = Article.objects.all().order_by('id')
    paginator = Paginator(articles,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'articles/articlespage.html',{'page_obj': page_obj})

def detail(request,slug):
    page_obj = Article.objects.get(id=slug)
    return render(request,'articles/article.html',{'page_obj':page_obj})


@login_required(login_url="/users/login/")
def create(request):
    if request.method == 'POST':
        form = forms.Create(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:articles')
    else:
        form = forms.Create()
    return render(request, 'articles/create.html', { 'form': form })

