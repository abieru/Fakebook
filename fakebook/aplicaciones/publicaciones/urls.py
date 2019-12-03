from django.urls import path
from .views import PostListView, PostDetailView, PostCreate, PostUpdate, PostDelete

post_patterns = ([
    path('', PostListView.as_view(), name='posts'),
    path('<username>/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='create'),
    path('update/<username>/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('delete/<username>/<int:pk>/', PostDelete.as_view(), name='delete'),
], 'post')