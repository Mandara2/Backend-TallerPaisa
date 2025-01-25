from django.urls import path, include
from rest_framework import routers
from apps.crud.views.customerView import CustomerView

router = routers.DefaultRouter()
router.register(r'', CustomerView, 'customer')

urlpatterns = [
    path('', include(router.urls))
]