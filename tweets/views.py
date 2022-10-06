from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .forms  import TweetModelForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

def home(request):
    return render(request, 'tweets/home.html')

def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    context = {
        "object":obj,
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):

    def get_queryset(*args, **kwargs):
        qs = Tweet.objects.all()#Seleccionamos todos los valores
        query = request.GET.get("q" or None)#Seleccionamos el valor q de la url
        if query:
            qs = qs.filter(content__icontains=query)#Filtramos en base a el q obtenido de la url
        return qs #Se retornan los valores a la vista
    
    form = TweetModelForm
    url_form = reverse_lazy("tweet_create")
    context = {
        "objects":get_queryset(),
        "form":form,
        "url_form": url_form,
    }
    return render(request, "tweets/list_view.html", context)

    def get_absolute_url(self):
        return reverse('tweet_update', kwargs={"pk", self.pk})

def tweet_create_view(request):
    form = TweetModelForm(request.POST)
    if form.is_valid() and request.user.is_authenticated:
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

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_view.html'
    success_url = reverse_lazy("tweet_list")
