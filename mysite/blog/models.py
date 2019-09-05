from django.db import models

# Create your models here.
class Article(models.Model):
    # 创建文章数据表
    title=models.CharField(max_length=32,default="Title")
    content=models.TextField(null=True)
