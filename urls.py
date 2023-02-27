from django.urls import include, path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('api/blogs/', BlogList.as_view(), name='blog-list'),
    path('api/blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('', include('blogs.urls')),
]
