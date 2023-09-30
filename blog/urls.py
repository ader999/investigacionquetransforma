from django.urls import path
from blog import views


app_name = 'mi_proyecto'  # Define el espacio de nombres

urlpatterns = [
    path('', views.blog_app, name='blog_app'),
    path('<int:id>/', views.detalle_de_entrada, name='detalle_de_entrada'),
    path('volver_app_inicio/', views.volver_app_inicio, name='volver_app_inicio'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),


    # Agrega más rutas URL según las necesidades de tu blog
]
