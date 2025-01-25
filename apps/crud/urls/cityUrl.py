from django.urls import path, include
from rest_framework import routers
from apps.crud.views.cityView import CityView

router = routers.DefaultRouter()
router.register(r'', CityView, 'city')

urlpatterns = [
    path('', include(router.urls))
]