from django.contrib import admin

# Register your models here.
from .models import StreetModel, StreetPhoto


class StreetPhotoAdmin(admin.TabularInline):
    model = StreetPhoto


@admin.register(StreetModel)
class StreetModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [StreetPhotoAdmin]
