from django.contrib import admin
from myapp.models import user,Product,Appointment

# Register your models here.
admin.site.register(user)
admin.site.register(Product)
admin.site.register(Appointment)



