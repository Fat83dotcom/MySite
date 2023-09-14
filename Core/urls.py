from django.urls import path
from Core.views import IndexView, BlogView, PortfolioView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('about/', AboutView.as_view(), name='about'),
]
