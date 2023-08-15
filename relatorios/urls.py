from django.urls import path
from . import views

urlpatterns = [
    path('', views.relatorio_inicio, name="relatorio_inicio"),
    path('novo_relatorio/', views.novo_relatorio, name="novo_relatorio"),
    path('listar_relatorio/', views.listar_relatorio, name="listar_relatorio"),
    path('relatorio/<str:identificador>/', views.relatorio, name="relatorio"),
    path('baixar_os/<str:identificador>/', views.baixar_os, name="baixar_os"),
]
