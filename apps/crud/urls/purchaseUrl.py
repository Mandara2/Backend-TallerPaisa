from django.urls import path, include
from rest_framework import routers
from apps.crud.views.purchaseView import PurchaseView

router = routers.DefaultRouter()
router.register(r'', PurchaseView, 'purchase')

urlpatterns = [
    path('', include(router.urls))
]