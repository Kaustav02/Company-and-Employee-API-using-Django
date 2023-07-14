from django.contrib import admin
from api.models import company,employee

class CompnayAdmin(admin.ModelAdmin):
    list_display=('name','location','type')



class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','company')
    
    
    
admin.site.register(company,CompnayAdmin)
admin.site.register(employee,EmployeeAdmin)


# Register your models here.
