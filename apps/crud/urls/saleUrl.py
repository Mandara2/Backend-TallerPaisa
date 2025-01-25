from django.urls import path, include
from rest_framework import routers
from apps.crud.views.saleView import SaleView

router = routers.DefaultRouter()
router.register(r'', SaleView, 'sale')

urlpatterns = [
    path('', include(router.urls))
]