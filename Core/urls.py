from django.urls import path
from Core.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
