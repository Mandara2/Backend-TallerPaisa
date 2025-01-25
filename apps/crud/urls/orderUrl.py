from django.urls import path, include
from rest_framework import routers
from apps.crud.views.orderView import OrderView

router = routers.DefaultRouter()
router.register(r'', OrderView, 'order')

urlpatterns = [
    path('', include(router.urls))
]