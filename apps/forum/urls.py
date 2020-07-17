from django.urls import path,include
from .views import ForumCreate,ForumListView,ForumUserListView,ForumDetailView

urlpatterns = [
    path("",ForumListView.as_view(),name="forum-list"),
    path("add/", ForumCreate.as_view(), name="forum-add"),
    path("<slug:slug>/",ForumDetailView.as_view(),name="forum-detail"),
    path("by/<username>/", ForumUserListView.as_view(), name="forum-by"),
]