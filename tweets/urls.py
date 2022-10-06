"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import tweet_detail_view, tweet_list_view, tweet_create_view, TweetUpdateView, TweetDeleteView, home
from rest_framework import routers
from .viewset import TweetViewSet

router = routers.DefaultRouter()
router.register('tweets', TweetViewSet)

urlpatterns = [
    path('home/', home, name="home"),
    path('create/', tweet_create_view, name="tweet_create"),
    path('list/', tweet_list_view, name="tweet_list"),
    path('detail/<id>/', tweet_detail_view, name="tweet_detail"),
    path('update/<pk>/', TweetUpdateView.as_view(), name="tweet_update"),
    path('delete/<pk>/', TweetDeleteView.as_view(), name="tweet_delete"),
    path('api/v1.0/', include(router.urls)),
]
