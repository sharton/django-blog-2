from django.urls import path
from . import views

urlpatterns = [
  path('', views.PostListView.as_view(), name='post_list'),
  path('drafts/', views.DraftPostListView.as_view(), name='draft_list'),
  path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
  path('new/', views.PostCreateView.as_view(), name='post_create'),
  path('<int:pk>/edit', views.PostUpdateView.as_view(), name='post_update'),
  path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
