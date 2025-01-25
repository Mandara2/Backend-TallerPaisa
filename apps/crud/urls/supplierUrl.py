from django.urls import path, include
from rest_framework import routers
from apps.crud.views.supplierView import SupplierView

router = routers.DefaultRouter()
router.register(r'', SupplierView, 'supplier')

urlpatterns = [
    path('', include(router.urls))
]