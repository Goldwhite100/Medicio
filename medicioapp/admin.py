from django.contrib import admin
from medicioapp.models import Product,Branch,Contact,Appoint,Member

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Appoint)
admin.site.register(Branch)
admin.site.register(Member)














#python3 manage.pymakemigrations
#-------------migrate
#runserver