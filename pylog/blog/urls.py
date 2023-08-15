from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list),
    path('<int:isthis>/', views.post_detail),
    path('upload/', views.post_upload),
    path('<int:isthis>/update/', views.post_update),
    path('<int:isthis>/delete/', views.post_delete),
]