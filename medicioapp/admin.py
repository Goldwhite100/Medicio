from django.contrib import admin
from medicioapp.models import Product,Branch,Contact,Appoint

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Appoint)
admin.site.register(Branch)














#python3 manage.pymakemigrations
#-------------migrate
#runserver