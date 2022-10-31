from django.urls import path
from .views import homePageView, aboutePageView

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('aboute/', aboutePageView.as_view(), name='aboute')
]