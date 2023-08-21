from django.contrib import admin
from .models import Person
from .models import Reservation
# Register your models here.

admin.site.register(Reservation)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith", )