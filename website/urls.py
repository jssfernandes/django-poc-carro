from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('/carros', views.home_carros, name='home_carros'),
    path('carros', views.CarroIndex.as_view(), name='home_carros'),
    path('carros/cadastro', views.CarroCreate.as_view(), name='cadastro_carros'),
    path('carros/<int:pk>', views.CarroUpdate.as_view(), name='update_carros'),
    # path('/fabricantes', views.home_fabricantes, name='home_fabricantes'),
    path('fabricantes', views.FabricanteIndex.as_view(), name='home_fabricantes'),
    # path('cadastro/fabricantes', views.FabricanteCreate.as_view(), name='cadastro_fabricantes'),
    path('fabricantes/cadastro', views.FabricanteCreate.as_view(), name='cadastro_fabricantes'),
    path('fabricantes/<int:pk>', views.FabricanteUpdate.as_view(), name='update_fabricantes'),
]