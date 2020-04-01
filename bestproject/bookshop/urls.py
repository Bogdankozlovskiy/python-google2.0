from django.urls import re_path
from bookshop import views

urlpatterns = [
        re_path(r'^$', views.hello),
        re_path(r"^world/$", views.world, name="world_page"),
        re_path(r"^just_url/(?P<id_book>[\d]+)/$",
                views.comment_handler, name="comment_url"),
]
