from django.urls import path
from . import views
from .views import line_chart, line_chart_json

urlpatterns = [
    path('', views.charts, name="Charts"),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
]