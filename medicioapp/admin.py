from django.contrib import admin
from medicioapp.models import Product,Branch,Contact

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)














#python3 manage.pymakemigrations
#-------------migrate
#runserver