from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from Core.models import Post
from django.db.models import Q


PER_PAGE = 9


class IndexView(View):
    def get(self, request):
        return render(request, 'site/index.html')


class BlogView(View):
    def get(self, request):
        result = Post.objects.getIsPublished()
        paginator = Paginator(result, PER_PAGE)
        pageNumber = request.GET.get('page')
        pageObj = paginator.get_page(pageNumber)
        context = {
            'posts': pageObj,
        }
        return render(request, 'blog/blogIndex.html', context)


class BlogPostView(View):
    def get(self, request, slug):
        result = Post.objects.get(slug=slug)
        context = {
            'post': result,
        }
        return render(request, 'blog/post.html', context)


class CategoryView(View):
    def get(self, request, slug):
        result = Post.objects.getIsPublished().filter(
            categoryKey__slug=slug
        )
        paginator = Paginator(result, PER_PAGE)
        pageNumber = request.GET.get('page')
        pageObj = paginator.get_page(pageNumber)
        context = {
            'posts': pageObj,
        }
        return render(request, 'blog/blogIndex.html', context)


class TagView(View):
    def get(self, request, slug):
        result = Post.objects.getIsPublished().filter(
            tagKey__slug=slug
        )
        context = {
            'posts': result,
        }
        return render(request, 'blog/blogIndex.html', context)


class SearchView(View):
    def get(self, request):
        search: str = request.GET.get('search').strip()
        result = Post.objects.getIsPublished().filter(
            Q(title__icontains=search) |
            Q(excerpt__icontains=search) |
            Q(content__icontains=search)
        )
        paginator = Paginator(result, PER_PAGE)
        pageNumber = request.GET.get('page')
        pageObj = paginator.get_page(pageNumber)
        context = {
            'posts': pageObj,
        }
        return render(request, 'blog/blogIndex.html', context)


class PortfolioView(View):
    def get(self, request):
        return render(request, 'portfolio/portfolio.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about/about.html')
