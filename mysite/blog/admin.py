from django.contrib import admin
# 用当前所在目录导入
from .models import Article
# 用项目默认路径导入
from mysite.blog.models import Article
# Register your models here.
admin.site.register(Article)
