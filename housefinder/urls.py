"""housesearch URL Configuration

"""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from listings import views
from django.conf.urls import include

urlpatterns = [
    path('', include('listings.urls'))
]
