from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name = 'home'),
    path('about-us/', AboutUsView.as_view(), name = 'about-us'),
]