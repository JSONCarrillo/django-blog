from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('article/<int:pk>/', articleView.as_view(), name='article'),
    path('add-post/', addPostView.as_view(), name='add-post'),
    path('add-category/', addCategoryView.as_view(), name='add-category'),
    path('article/<int:pk>/update/', updatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete/', deletePostView.as_view(), name='delete-post'),
    path('category/<str:category>/', categoryView, name='categories'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(),name="edit-profile"),
]