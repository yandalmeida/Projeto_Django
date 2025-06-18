from django.contrib import admin
from .models import Livro
from .models import Cliente

# Register your models here.
admin.site.register(Livro)
admin.site.register(Cliente)