from django.urls import path
from . import views

urlpatterns = [
    path('', views.autorizacao, name="autorizacao"),
    path('atualiza_autorizacao/', views.att_autorizacao, name="atualiza_autorizacao"),
    path('update_autorizacao/<int:id>', views.update_autorizacao, name="update_autorizacao"),
    path('listar_autorizacao/', views.listar_autorizacao, name="listar_autorizacao"),
    path('autorizacao_list/<str:id>/', views.autorizacao_list, name="autorizacao_list"),
    path('baixar/<str:id>/', views.baixar, name="baixar"),
]
