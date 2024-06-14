from django.urls import path
from . import views
# Create your views here.
app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
]
