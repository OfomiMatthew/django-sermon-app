from django.urls import path 
from .views import *

urlpatterns = [
    path('login/',SermonLoginView.as_view(),name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
]
