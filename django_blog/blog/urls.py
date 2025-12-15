from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,    
    CommentUpdateView,
    CommentCreateView,
    CommentDeleteView,
    PostByTagListView,
)

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),

    # CRUD URLs required by checker
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

     # Comments: add, edit, delete
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(),
         name="comment-create"),  # Required pattern

    path("comment/<int:pk>/update/", CommentUpdateView.as_view(),
         name="comment-update"),  # Required pattern

    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(),
         name="comment-delete"),

    path("tags/<str:tag_name>/", views.tagged_posts, name="posts-by-tag"),
    path("search/", views.search, name="search"),

    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]