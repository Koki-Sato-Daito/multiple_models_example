from django.urls import path, include

from apiv1.views import ItemListAPIView


urlpatterns = [
    path('items/', ItemListAPIView.as_view())
]
