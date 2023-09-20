from django.urls import path
from Core.views import IndexView, PortfolioView, AboutView
from Core.views import BlogPostView, BlogView, CategoryView
from Core.views import TagView, SearchView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blogIndex'),
    path('blog/post/<slug:slug>/', BlogPostView.as_view(), name='blogPost'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('tag/<slug:slug>/', TagView.as_view(), name='tag'),
    path('search/', SearchView.as_view(), name='search'),
]
