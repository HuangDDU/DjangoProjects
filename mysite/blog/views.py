from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator


# Create your views here.
def index(request, page):  # 给定页数
    # 接收到HTTP的POST请求用来新建或修改博客成功
    # 指定page_num到分页的第几页
    print("进入主页")
    if request.POST.get('title', '') != '':
        # 如果接收到了POST请求
        id = request.POST['id']
        title = request.POST['title']
        content = request.POST['content']
        if id == '0':
            # 如果新建博客
            Article.objects.create(title=title, content=content)
        else:
            # 如果是修改博客，从数据库里取出来，并且修改后存到数据库里
            edited_article = Article.objects.get(pk=id)
            edited_article.title = title
            edited_article.content = content
            edited_article.save()
    # 展示所有数据
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 3)  # 此处每页指定元素数目
    pages_num = paginator.num_pages  # 一共有这么多页
    articles = paginator.page(page)  # 当前分页的文章
    # 如果是第一页或者最后一页，上一篇或者下一页就是自己
    if articles.has_previous():
        previous_page = str(int(page) - 1)
    else:
        previous_page = page
    if articles.has_next():
        next_page = str(int(page) + 1)
    else:
        next_page = page

    return render(request, 'blog/index.html', {'articles': articles,  # 当前分页的文章
                                               'pages_num': range(1, pages_num + 1),  # 从1到page_num的列表
                                               'current_page': page,  # 当前的页码
                                               'previous_page': previous_page,  # 下一页页码
                                               'next_page': next_page,
                                               })


def detail(request, article_id):
    articles = Article.objects.all()
    # 如果是第一篇或者最后一篇，上一篇或者下一篇就是自己
    if article_id == str(1):
        # 如果是第一篇
        previous_article_id = str(article_id)
    else:
        previous_article_id = str(int(article_id) - 1)
    if article_id == str(len(articles)):
        # 如果是最后一篇
        next_article_id = str(article_id)
    else:
        next_article_id = str(int(article_id) + 1)
    # 分别获得当前文章、上一篇、下一篇文章
    article = Article.objects.get(pk=article_id)
    previous_article = Article.objects.get(pk=previous_article_id)
    next_article = Article.objects.get(pk=next_article_id)

    return render(request, "blog/detail.html", {"article": article,
                                                "previous_article": previous_article,
                                                "next_article": next_article,
                                                })


def new_blog(request, article_id):
    if article_id == '0':
        return render(request, "blog/new_blog.html")
    else:
        article = Article.objects.get(pk=article_id)
        return render(request, "blog/new_blog.html", {"article": article})
