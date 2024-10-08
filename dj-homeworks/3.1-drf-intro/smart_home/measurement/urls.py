from django.conf import settings
from django.urls import path
from .views import SensorView, SensorDetailView, MeasurementsAddView


urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementsAddView.as_view())
]
