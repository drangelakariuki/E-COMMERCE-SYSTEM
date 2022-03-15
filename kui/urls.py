from django.urls import path
from . import views
# urlconf model
urlpatterns = [
    path('hello/', views.say_hello),
    path('index/', views.check_base),
    ]
