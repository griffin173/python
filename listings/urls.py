from django.urls import path
from listings import views
from django.conf.urls import include

urlpatterns = [
    path('listings/', views.ListingList.as_view()),
    path('listings/<int:pk>/', views.ListingDetail.as_view()),
    path('upload/<filename>/', views.ImportView.as_view()),
]