from django.urls import path
from .views import SilaboList, SilaboDetail

urlpatterns = [
    path('silabos/', SilaboList.as_view(), name='silabo-list'),
    path('silabos/<int:pk>/', SilaboDetail.as_view(), name='silabo-detail'),
]

