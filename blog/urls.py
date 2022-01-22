from django.urls import path

from blog import views
from blog.views import *

app_name = "blog"

urlpatterns = [
    path("", post_list, name='post_list'),
    # path("<int:year>/<int:month>/<int:day>/<slug:post>/",
    #      post_detail.as_view(),
    #      name='post_detail'),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/",
         PostListView.as_view(),
         name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share')
]