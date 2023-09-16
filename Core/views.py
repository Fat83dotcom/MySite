from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'site/index.html')


class BlogView(View):
    def get(self, request):
        return render(request, 'blog/blogIndex.html')


class BlogPageView(View):
    def get(self, request):
        return render(request, 'blog/page.html')


class BlogPostView(View):
    def get(self, request):
        return render(request, 'blog/post.html')


class PortfolioView(View):
    def get(self, request):
        return render(request, 'portfolio/portfolio.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about/about.html')
