from .views import BalanceViewset, CapitalViewset, ExcelViewset
from django.urls import path, include

from rest_framework import routers


router = routers.DefaultRouter()
router.register('balance', BalanceViewset)
router.register('capital', CapitalViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('upload_excel', ExcelViewset.as_view()),

]
