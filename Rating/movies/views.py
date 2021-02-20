from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *


def LoginPage(request,*args,**kwargs):
    if request.method == "POST":
        username = request.POST.get('email',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html', {'errors':True})
    return render(request,'login.html')


@login_required
def Homepage(request):
    data = Movies.objects.all()
    context = {
        'data': data
    }
    return render(request, 'homepage-1.html',context)

@login_required
def View_Movie(request,pk):
    try:
        data = Movies.objects.get(id=pk)
        latest_movies = Movies.objects.all()[:3]
        context = {
            'movie': data,
            'latest_movies':latest_movies
        }
        return render(request,'article-sidebar-right.html',context)
    except:
        return render(request,"404.html")

@login_required
def WriteComments(request,pk):
    try:
        data = Movies.objects.get(id=pk)
        review = request.POST.get("review",None)
        rating = request.POST.get("rating",None)
        print(review,rating)
        movie = Comments(review = review)
        movie.Rating = rating
        movie.movie = data
        print(request.user)
        movie.Author = request.user
        movie.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def logout_view(request):
    logout(request)
    return redirect("login")

