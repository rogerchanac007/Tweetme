from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .forms  import TweetModelForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    context = {
        "object":obj,
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):

    def get_queryset(*args, **kwargs):
        qs = Tweet.objects.all()
        query = request.GET.get("q" or None)
        if query:
            qs = qs.filter(content__icontains=query)
        return qs
    
    context = {
        "objects":get_queryset(),
    }
    return render(request, "tweets/list_view.html", context)

def tweet_create_view(request):
    form = TweetModelForm(request.POST)
    if form.is_valid() and request.user.authenticated():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("tweet_list")
    context = {
        "form":form,
    }

    return render(request, "tweets/create_view.html", context)

class TweetUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = "/tweets/list"
    login_url = "/admin/"

class TweetDeleteView(DeleteView):
    model = Tweet
    template_name = 'tweets/delete_view.html'
    success_url = reverse_lazy("tweet_list")
