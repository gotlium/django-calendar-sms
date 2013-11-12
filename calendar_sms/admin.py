# -*- coding: utf-8 -*-

from django.contrib import admin

from models import (CalendarSMSLogs, CalendarSMSWebsites, CalendarSMSSettings)
from forms import CalendarSMSSettingsForm


class CalendarSMSSettingsInline(admin.TabularInline):
    model = CalendarSMSSettings
    extra = 1
    form = CalendarSMSSettingsForm


class CalendarSMSLogsAdmin(admin.ModelAdmin):
    search_fields = ('title', 'message',)
    list_display = (
        'email', 'title', 'content', 'status', 'created', 'updated',
    )
    list_display_links = ('title',)
    list_filter = ('status', 'created', 'updated', 'email__website', 'email')
    ordering = ('created',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def __init__(self, model, admin_site):
        admin.ModelAdmin.__init__(self, model, admin_site)
        self.readonly_fields = [field.name for field in model._meta.fields]
        self.readonly_model = model


class CalendarSMSWebsitesAdmin(admin.ModelAdmin):
    search_fields = ('website',)
    list_display = (
        'site', 'status', 'created', 'updated', 'id',
    )
    list_display_links = ('site',)
    list_filter = ('status', 'created', 'updated')
    fields = ('site', 'status',)
    ordering = ('created',)
    inlines = (CalendarSMSSettingsInline,)


admin.site.register(CalendarSMSLogs, CalendarSMSLogsAdmin)
admin.site.register(CalendarSMSWebsites, CalendarSMSWebsitesAdmin)
