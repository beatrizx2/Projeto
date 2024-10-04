from django.contrib import admin
from .models import User #importar nossos modelos 
# Register your models here.

admin.site.register(User) #colocar nossa classe criada no models
