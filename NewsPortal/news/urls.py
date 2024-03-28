from django.urls import path
from .views import PostsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, ArticlesPostCreate, \
    CategoryListView, subscribe

urlpatterns = [
    path('news/', PostsList.as_view(), name='posts_list'),
    path('news/search/', PostSearch.as_view(), name='posts_search'),
    path('news/<int:pk>', PostDetail.as_view(), name='posts_detail'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('news/categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('news/categories/<int:pk>/subscribe', subscribe, name='subscribe'),

    path('articles/create/', ArticlesPostCreate.as_view(), name='post_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
