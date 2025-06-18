from django import forms #Importar o forms
from .models import Livro, Cliente#Importa o modelo (ex: Livro)
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro #Modelo (Classe do model)
        fields = [
            'nome_livro',
            'nome_autor',
            'sobrenome_autor'
        ]

        #Opcional - Personlização do input do formulario
        widgets = {
            "nome_livro": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite o nome do livro"}),
            "nome_autor": forms.TextInput(attrs={"class":"form-control","placeholder": "Digite o nome do Autor"}),
            "sobrenome_autor": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite o sobrenome do Autor"})
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente #Modelo (Classe do model)
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'email'
        ]

        #Opcional - Personlização do input do formulario
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu nome"}),
            "sobrenome": forms.TextInput(attrs={"class":"form-control","placeholder": "Digite seu Sobrenome"}),
            "cpf": forms.TextInput(attrs={"class": "form-control","placeholder": "___.___.___-__"}), # Exemplo de placeholder para CPF
            "email": forms.EmailInput(attrs={"class": "form-control","placeholder": "email@example.com"}), # Usando EmailInput
        }