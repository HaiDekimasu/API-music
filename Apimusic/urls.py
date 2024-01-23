from django.urls import path, include
from rest_framework import routers
from Apimusic import views

router=routers.DefaultRouter()
router.register(r'Apimusic', views.MusicViewSet)

urlpatterns = [
    path('', include(router.urls))
]

