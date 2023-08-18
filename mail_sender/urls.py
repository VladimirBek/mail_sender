from django.urls import path
from views import IndexList

urlpatterns = [
    path('', IndexList.as_view(), name='index')
]
