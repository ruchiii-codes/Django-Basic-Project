# from django.urls import path
from . import views

# #URLConf
# urlpatterns = [
#     path('hallo/', views.say_hello)
# ]

from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
]
