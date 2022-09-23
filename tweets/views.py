from django.shortcuts import render, redirect
from .models import Tweet
from .forms  import TweetModelForm

def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    context = {
        "object":obj,
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "objects":queryset,
    }
    return render(request, "tweets/list_view.html", context)

def tweet_create_view(request):
    form = TweetModelForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("tweet_list")
    context = {
        "form":form,
    }

    return render(request, "tweets/create_view.html", context)
