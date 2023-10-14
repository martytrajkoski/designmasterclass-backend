from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Purchase
from .models import Course
from .models import Tutorial

admin.site.register(Customer)
admin.site.register(Course)
admin.site.register(Purchase)
admin.site.register(Tutorial)