from django.urls import path
from . import views

urlpatterns = [
    path('pages/', views.inicio, name="Inicio"),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path("post/", views.post_view, name= "post"),
    path("user_post/", views.view_name, name= "postusuario"),
    path('article/<int:article_id>', views.article_view, name='article_view'),
    path('upload/', views.upload_avatar, name='upload_avatar'),
]
