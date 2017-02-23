from django.contrib import admin
from .models import Phone, CostomOption, PhoneSold, Repository

#admin.site.register(Repository)


class PhonesInline(admin.TabularInline):
    model = Phone
    list_display_links = ['modell']


class CostomOptionAdmin(admin.ModelAdmin):
    list_display = ('modell', 'cpu', 'RAMmemory', 'internalmemory', 'qualitycamera')
    list_editable = ["cpu"]
    search_fields = ['modell']


admin.site.register(CostomOption, CostomOptionAdmin)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'costomoption', 'description')


@admin.register(PhoneSold)
class PhoneSoldAdmin(admin.ModelAdmin):
    list_display = ('product', 'buyer', 'time_of_purchase', 'phonenumber', 'address', 'email')


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('phone', 'numbers', 'costomoption', 'get_pk', 'status')
    list_filter = ('phone__costomoption', 'status')
