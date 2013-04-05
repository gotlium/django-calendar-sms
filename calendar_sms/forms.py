# -*- coding: utf-8 -*-

from django import forms

from models import CalendarSMSSettings


class CalendarSMSSettingsForm(forms.ModelForm):
    class Meta:
        model = CalendarSMSSettings
        widgets = {
            'password': forms.PasswordInput()
        }
