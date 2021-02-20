from django.urls import path, include
from .views import *
urlpatterns = [
    path('', LoginPage, name='login'),
    path('Dashboard', Homepage, name='home'),
    path("movie/view/<int:pk>",View_Movie, name="movie"),
    path("movie/comment/<int:pk>",WriteComments,name="comment"),
    path("logout",logout_view,name="logout")
] 


