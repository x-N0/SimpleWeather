from django.conf.urls import url
from .views import Home

urlpatterns = [
    url(r'', Home, 'Index')
]
