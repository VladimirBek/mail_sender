from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogPublishView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', cache_page(60)(BlogListView.as_view()), name='blogs'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_details/<int:pk>/', BlogDetailView.as_view(), name='blog_details'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blogs/<int:pk>/publish/', BlogPublishView.as_view(), name='blog_publish'),

]