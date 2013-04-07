# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.db import models


class AbstractCalendarSMS(models.Model):
    status = models.BooleanField(_('Status'), default=True)
    created = models.DateTimeField(
        _('Created'), auto_now=False, auto_now_add=True,
        db_index=True, editable=False)
    updated = models.DateTimeField(
        _('Updated'), auto_now=True, auto_now_add=True,
        db_index=True, editable=False)

    class Meta:
        abstract = True


class CalendarSMSWebsites(AbstractCalendarSMS):
    site = models.ForeignKey(Site, verbose_name=_('Website'), default=1)

    def __unicode__(self):
        return self.site.domain

    class Meta:
        db_table = 'calendar_sms_websites'
        verbose_name = _('Websites')
        verbose_name_plural = _('Websites')


class CalendarSMSSettings(AbstractCalendarSMS):
    email = models.CharField(_('Google account'), max_length=250)
    password = models.CharField(
        _('Account password'), max_length=250,
        help_text=_('That is application password, not from a mail account'))
    calendar = models.CharField(
        _('Calendar ID'), max_length=250, blank=True, null=True,
        help_text=_('For example: fafgttkq8ed2idfgd@group.calendar.google.com.'
                    'You can view the calendar settings - details specific '
                    'calendar field "Calendar Address" and right there in '
                    'the brackets.'))
    start_time = models.PositiveIntegerField(
        _('Event starts'), default=120, max_length=3,
        help_text=_('Specifies how long the event will begin (in seconds)'))
    end_time = models.PositiveIntegerField(
        _('End of event'), default=180, max_length=3,
        help_text=_(
            'Specifies how long the event will be complete (in seconds)'
        ))
    reminder_time = models.PositiveIntegerField(
        _('Reminder time'), default=1, max_length=2,
        help_text=_('Reminder time in minutes'))
    attempts = models.PositiveIntegerField(
        _('Numbers of attempts'), default=2, max_length=2,
        help_text=_('Max number of attempts to establish a new '
                    'memo to the calendar'))
    delays = models.PositiveIntegerField(
        _('Delays'), default=5, max_length=1,
        help_text=_('Waiting time between attempts'))
    website = models.ForeignKey(CalendarSMSWebsites)

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'calendar_sms_settings'


class CalendarSMSLogs(AbstractCalendarSMS):
    title = models.CharField(_('Title'), max_length=160)
    content = models.CharField(
        _('Message'), max_length=350, blank=True, null=True)
    email = models.ForeignKey(CalendarSMSSettings, verbose_name=_('Email'))

    def __unicode__(self):
        return '%s / %s' % (self.email, self.title)

    class Meta:
        db_table = 'calendar_sms_logs'
        ordering = ['-created']
        verbose_name = _('SMS Logs')
        verbose_name_plural = _('SMS Logs')
