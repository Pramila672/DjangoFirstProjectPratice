from django.contrib import admin
from .models import Person 
from .import models             

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstname' , 'lastname', 'age', 'created_date')

admin.site.register(models.Person, PersonAdmin)
#admin.site.register(models.Profile)