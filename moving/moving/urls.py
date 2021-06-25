from django.urls import path, include

urlpatterns = [
    path('moving', include('information.urls')),
]
