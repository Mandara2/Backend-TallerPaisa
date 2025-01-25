from django.urls import path, include
from rest_framework import routers
from apps.crud.views.branchView import BranchView

router = routers.DefaultRouter()
router.register(r'', BranchView, 'branch')

urlpatterns = [
    path('', include(router.urls))
]