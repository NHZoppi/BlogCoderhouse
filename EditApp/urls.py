from . import views
from django.urls import path
from .views import UpdateProfileView, ChangePasswordView, PostDeleteView

urlpatterns = [
    path("Change_profile/", UpdateProfileView.as_view(), name= "chprofile"),
    path("Change_pass/", ChangePasswordView.as_view(), name= "chpass"),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete")
]