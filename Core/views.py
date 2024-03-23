from typing import Any
from Core.models import Post, Portfolio, PortfolioProjects
from django.views import View
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView


PER_PAGE = 9


class IndexView(View):
    title = 'Home'

    def get(self, request):
        return render(request, 'site/index.html', {'title': self.title})


class BlogView(ListView):
    model = Post
    template_name = 'blog/blogIndex.html'
    context_object_name = 'posts'
    ordering = '-id',
    paginate_by = PER_PAGE
    title = 'Artigos'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Post.objects.getIsPublished()
        return queryset


class BlogPostView(DetailView):
    slug_field = 'slug'
    context_object_name = 'post'
    template_name = 'blog/post.html'
    queryset = Post.objects.getIsPublished()
    title = 'Artigo'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(slug=self.kwargs.get('slug'))
        return queryset


class CategoryView(BlogView):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            categoryKey__slug=self.kwargs.get('slug')
        )
        return queryset


class TagView(BlogView):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            tagKey__slug=self.kwargs.get('slug')
        )
        return queryset


class SearchView(BlogView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__search = None

    def get(self, request, *args, **kwargs):
        self.__search = request.GET.get('search').strip()
        if self.__search == '' or self.__search is None:
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            Q(title__icontains=self.__search) |
            Q(excerpt__icontains=self.__search) |
            Q(content__icontains=self.__search)
        )
        return queryset


class PortfolioView(View):
    template_name = 'portfolio/portfolio.html'
    title = 'Portfólio'

    def get(self, request, *args, **kwargs):
        result = Portfolio.objects.all().first()
        print(result)
        context = {
            'portf': result,
            'title': self.title,
        }
        return render(request, self.template_name, context)


class PortfolioProjectView(DetailView):
    model = PortfolioProjects
    template_name = 'portfolio/project.html'
    context_object_name = 'project'
    slug_field = 'slug'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(slug=self.kwargs.get('slug'))
        return queryset


class AboutView(View):
    title = 'Contato'

    def get(self, request):
        return render(request, 'about/about.html', {'title': self.title})
