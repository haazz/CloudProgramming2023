# urlconf for blog
from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_num>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    #path('<int:post_num>/', views.single_post_page),
]
