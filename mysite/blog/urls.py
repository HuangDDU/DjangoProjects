from django.urls import path,re_path
from . import views

urlpatterns = [
    # 主页面
    re_path("index/(?P<page>[0-9]+)/", views.index, name="index"),
    # 每个博客的详细页面
    re_path("(?P<article_id>[0-9]+)/", views.detail, name="detail"),
    # 博客新建\修改页面
    path("new_blog/(?P<article_id>[0-9]+)/", views.new_blog, name="new_blog")
]