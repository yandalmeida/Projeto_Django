from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View #Listview - Lista os dados a partir de uma classe
from django.urls import reverse_lazy
from .models import Livro, Cliente
from .forms import LivroForm    


# Create your views here.

#Classe da pagina principal
class Home(ListView):
    def get(self,request):
        return render(request, 'Blog/home_blog.html')

class Livros_list(ListView):
    #a ferramenta listview permite (model,template_name)
    #Conecta ao modelo de banco de dados
    model = Livro #retorna uma lista chamamda cliente_list

    #Conecta ao arquivo html do templates
    template_name = 'Blog/list_livro.html'

class Cadastro(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'Blog/forms_livro.html'   #Gera o template do formulario
    success_url = reverse_lazy('lista_livro') #Redireciona para a pagina da tabela apos o cadastro

class Editar(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'Blog/forms_livro.html'
    success_url = reverse_lazy('lista_livro')

class Deletar(DeleteView):
    model = Livro
    template_name = 'Blog/delete_livro.html'
    success_url = reverse_lazy('lista_livro')

    #Trabalhando com sessoes
class BuscaCliente(View):
    #metodo que renderiza nosso formulario de autenticação
    def get(self, request):
        return render(request, 'Blog/livro_busca_form.html')
    
    #A partir daqui vamos:
    #Identificar o email e o cpf do formulario, 
    #identificar o cliente e criar a sessao
    def post(self, request):
        email = request.POST.get('email')#Guada email digitado no formulario
        cpf = request.POST.get('cpf')#Guarda cpf digitado no formulario

        if email and cpf: #verifica se o email e cpf existem
            #Guada as informações dos clientes (nosso_cliente)
            nosso_cliente = Cliente.objects.filter(email=email, cpf=cpf).first() #Pega o primerio cliente com o email e cpf
            if nosso_cliente: 
                #Vamos criar as sessoes
                request.session['nome_cliente'] = nosso_cliente.nome
                request.session['sobrenome_cliente'] = nosso_cliente.sobrenome
                titulo = 'Cliente encontrado!'
                return render(request, 'Blog/livro_busca_form.html',{'cliente':nosso_cliente, 'title':titulo})

            else: 
                erro_message = "Nenhum cliente encontrado."
                return render(request,'Blog/livro_busca_form.html', {'mensagem':erro_message})
        else: 
            erro_message = "Por favor, informe um email e cpf para consulta"
            return render(request, 'Blog/livro_busca_form.html', {'mensagem':erro_message})
        
#Calsse que encerra a sessão
class Logout(View):
    #Metodo que verifica e encerra a sessão
    def get(self, request):
        if 'nome_cliente' in request.session:
            del request.session['nome_cliente']
        if 'sobrenome_cliente' in request.session:
            del request.session['sobrenome_cliente']

        erro_message = 'Você foi desconectado!'
        return render(request, 'Blog/livro_busca_form.html', {'mensagem': erro_message})