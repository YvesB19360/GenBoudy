from django.contrib import admin

from boudy.models import Famille

class FamilleAdmin(admin.ModelAdmin):  
    list_display = ('nom', 'prenom') 

admin.site.register(Famille, FamilleAdmin)