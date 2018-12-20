from django.urls import path
from . import views

# This is For check
urlpatterns = [
    path('create/', views.post_create),
    path('detail/', views.post_detail),
    path('postlist/', views.post_list),
    path('update/', views.post_update),
    path('delete/', views.post_delete),
    # path('jango', views.index, name='jango'),
]
