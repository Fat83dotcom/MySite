from django.urls import path
from Core.views import IndexView, PortfolioView, AboutView
from Core.views import BlogPostView, BlogView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blogIndex'),
    path('blog/post', BlogPostView.as_view(), name='blogPost'),
]
