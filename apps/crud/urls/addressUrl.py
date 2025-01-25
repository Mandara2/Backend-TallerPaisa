from django.urls import path, include
from rest_framework import routers
from apps.crud.views.addressView import AddressView

router = routers.DefaultRouter()
router.register(r'', AddressView, 'address')

urlpatterns = [
    path('', include(router.urls))
]