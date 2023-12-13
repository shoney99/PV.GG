from django.contrib import admin
from django.urls import path, include
from mainApp import views

urlpatterns = [
    path(''              , views.mainpage),
    path('chart_inline/' , views.chart_inline),
    path('profile/'      , views.profile),
    path('widgets/'      , views.widgets),
    path('blank/'        , views.blank),
]