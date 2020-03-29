from django.urls import re_path
from bookshop import views

urlpatterns = [
        re_path('^$', views.hello),
        re_path("^world/$", views.world),
]
