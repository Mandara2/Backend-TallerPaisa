from django.urls import path, include
from rest_framework import routers
from apps.crud.views.categoryView import CategoryView

router = routers.DefaultRouter()
router.register(r'', CategoryView, 'category')

urlpatterns = [
    path('', include(router.urls))
]