from django.contrib import admin

from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "form", "name", "email")
    list_display_links = ("id", "name")
    search_fields = ("name", "year")
    list_filter = ("year", "form")

admin.site.register(Company, CompanyAdmin)


class ExpertAdmin(admin.ModelAdmin):
    list_display = ("id", "surname", "name", "last_name", "city", "email")
    list_display_links = ("id", "surname")
    search_fields = ("surname", "city")
    list_filter = ("city",)


admin.site.register(Expert, ExpertAdmin)


class BalanceAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "year", "comment")
    list_display_links = ("id",)
    search_fields = ("company", "year")
    list_filter = ("year", "company")


admin.site.register(Balance, BalanceAdmin)


class StatementAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "year", "comment")
    list_display_links = ("id",)
    search_fields = ("company", "year")
    list_filter = ("year", "company")


admin.site.register(Statement, StatementAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "date", "expert")
    list_display_links = ("id",)
    search_fields = ("company", "expert")
    list_filter = ("company", "expert")


admin.site.register(Report, ReportAdmin)
