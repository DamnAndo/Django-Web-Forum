from django.urls import path,include
from .views import (ForumCreate,ForumListView,ForumUserListView,
                    ForumDetailView,ForumUpdateView,ForumDeleteView,CommentCreate)

urlpatterns = [
    path("",ForumListView.as_view(),name="forum-list"),
    path("add/", ForumCreate.as_view(), name="forum-add"),
    path("edit/<int:pk>",ForumUpdateView.as_view(), name="forum-edit"),
    path("delete/<int:pk>", ForumDeleteView.as_view(), name="forum-delete"),
    path("<slug:slug>/",ForumDetailView.as_view(),name="forum-detail"),
    path("by/<username>/", ForumUserListView.as_view(), name="forum-by"),
    path("comment/add/<int:pk>",CommentCreate.as_view(), name="comment-add"),
    
]