from django.urls import path, include

urlpatterns = [
    path('', include('valid_app.urls')),
]
