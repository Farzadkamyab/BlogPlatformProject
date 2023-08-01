from django.urls import path
from .views import home, post_list,post_details,category_details,category_list, update_comment

urlpatterns = [
    path('', home, name="home"),
    path('post/', post_list, name="post_list"),
    path('post/<int:pk>/', post_details, name="post_details"),
    path('categories/', category_list, name="category_list"),
    path('categories/<int:pk>/', category_details, name="category_details"),
    path('update/', update_comment, name="update"),

]