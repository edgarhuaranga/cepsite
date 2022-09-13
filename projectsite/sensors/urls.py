from django.urls import path
from . import views
from .views import SensorItem
from .views import StartCEP
from .views import StopCEP

urlpatterns = [
    path('', views.index, name='index'),
    path('data', SensorItem.as_view()),
    path('start-cep', StartCEP.as_view()),
    path('stop-cep', StopCEP.as_view()),
]