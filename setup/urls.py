"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#Importar a função de views
from Blog.views import Livros_list,Home,Cadastro,Editar,Deletar,BuscaCliente,Logout

urlpatterns = [
    path('admin/', admin.site.urls),    
    
    #path da classe
    path('livro_home', Home.as_view(), name="home_blog"),
    path('livro_tabela/', Livros_list.as_view(), name="lista_livro" ),
    path('livro_form/', Cadastro.as_view(), name="livro_create"),
    path('livro_editar/<int:pk>', Editar.as_view(), name="livro_update"),
    path('livro_deletar/<int:pk>', Deletar.as_view(), name='livro_excluir'),
    path('',BuscaCliente.as_view(),name='busca_cliente'),
    path('cliente_sair/',Logout.as_view(), name='cliente_sair')
]
