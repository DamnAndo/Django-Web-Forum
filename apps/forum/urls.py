from django.urls import path,include
from .views import ForumCreate

urlpatterns = [
    path("add/",ForumCreate.as_view(),name="forum-add")
]