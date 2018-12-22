from django.urls import path
from . import views
from django.conf.urls import url

# This is For check
urlpatterns = [
    url('create/', views.post_create),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url('postlist/', views.post_list),
    url('update/', views.post_update),
    url('delete/', views.post_delete),
    # path('jango', views.index, name='jango'),
]
