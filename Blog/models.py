from django.db import models

# Create your models here.
class Livro(models.Model):
    # Campos que representam as colunas da tabela 'Livro' no banco de dados
    nome_livro = models.CharField(max_length=100) # Nome do livro, string de até 100 caracteres
    nome_autor = models.CharField(max_length=100) # nome do autor, string de até 100 caracteres
    sobrenome_autor = models.CharField(max_length=100) # sobrenome do autor, string de até 100 caracteres
    


    def __str__(self):
        """
        Método que retorna uma representação amigável do objeto Livro.
        Isso é útil no painel administrativo do Django e ao depurar.
        """
        return f"{self.nome_livro}"

    class Meta:
        """
        A classe Meta é uma classe interna que fornece metadados sobre o modelo.
        """
        verbose_name = "Livro" # Nome singular amigável para o modelo no painel administrativo
        verbose_name_plural = "Livros" # Nome plural amigável para o modelo no painel administrativo
        ordering = ['nome_livro'] # Define a ordem padrão dos registros ao consultá-los
        # Os registros serão ordenados primeiro pelo nome, depois pelo sobrenome.

class Cliente(models.Model):
    # Campos que representam as colunas da tabela 'Livro' no banco de dados
    nome = models.CharField(max_length=100) # Nome do livro, string de até 100 caracteres
    sobrenome = models.CharField(max_length=100) # Sobrenome do cliente, string de até 100 caracteres
    email = models.EmailField(unique=True) # Email do cliente, deve ser único e formatado como email
    cpf = models.CharField(max_length=11, unique=True) # CPF do cliente, string de 11 caracteres, deve ser único
    


    def __str__(self):
        """
        Método que retorna uma representação amigável do objeto Cliente.
        Isso é útil no painel administrativo do Django e ao depurar.
        """
        return f"{self.nome} {self.sobrenome} ({self.cpf})"

    class Meta:
        """
        A classe Meta é uma classe interna que fornece metadados sobre o modelo.
        """
        verbose_name = "Cliente" # Nome singular amigável para o modelo no painel administrativo
        verbose_name_plural = "Clientes" # Nome plural amigável para o modelo no painel administrativo
        ordering = ['nome', 'sobrenome'] # Define a ordem padrão dos registros ao consultá-los
        # Os registros serão ordenados primeiro pelo nome, depois pelo sobrenome.