from django.urls import path, include
from rest_framework import routers
from apps.crud.views.productView import ProductView

router = routers.DefaultRouter()
router.register(r'', ProductView, 'product')

urlpatterns = [
    path('', include(router.urls))
]