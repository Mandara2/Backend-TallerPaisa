from django.urls import path, include
from rest_framework import routers
from apps.crud.views.shoppingCartView import ShoppingCartView

router = routers.DefaultRouter()
router.register(r'', ShoppingCartView, 'shoppingCart')

urlpatterns = [
    path('', include(router.urls))
]