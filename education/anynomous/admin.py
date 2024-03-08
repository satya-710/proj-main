from django.contrib import admin

# Register your models here.
from .models import contact_master
admin.site.register(contact_master)


from .models import user_master
admin.site.register(user_master)


from.models import test_employee
admin.site.register(test_employee)