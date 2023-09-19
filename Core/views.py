from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from Core.models import Post


class IndexView(View):
    def get(self, request):
        return render(request, 'site/index.html')


class BlogView(View):
    def get(self, request):
        result = Post.objects.getIsPublished()
        paginator = Paginator(result, 9)
        pageNumber = request.GET.get('page')
        pageObj = paginator.get_page(pageNumber)
        context = {
            'posts': pageObj,
        }
        return render(request, 'blog/blogIndex.html', context)


class BlogPostView(View):
    def get(self, request):
        return render(request, 'blog/post.html')


class PortfolioView(View):
    def get(self, request):
        return render(request, 'portfolio/portfolio.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about/about.html')
