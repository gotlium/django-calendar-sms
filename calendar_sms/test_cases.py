# -*- coding: utf-8 -*-

import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site
from django.test import TestCase

from calendar_sms.sms import sendSMS
from calendar_sms.models import (
    CalendarSMSWebsites, CalendarSMSSettings, CalendarSMSLogs)


class CalendarSMSTestCase(TestCase):

    def setUp(self):
        self.email = 'gotlium.alerts@gmail.com'
        self.password = 'wjpnaqbuqlpdzssx'
        self.title = str(uuid.uuid4())

    def test_a_settings_is_set(self):
        self.assertRaises(ObjectDoesNotExist, sendSMS, self.title)

    def test_b_setup_website(self):
        CalendarSMSWebsites.objects.create(site=Site.objects.get(pk=1))
        self.assertEqual(CalendarSMSWebsites.objects.all().count(), 1)

    def test_c_setup_accounts(self):
        website = CalendarSMSWebsites.objects.create(
            site=Site.objects.get(pk=1))
        CalendarSMSSettings.objects.create(
            email=self.email,
            password=self.password,
            website=website
        )
        self.assertEqual(CalendarSMSSettings.objects.all().count(), 1)

    def test_d_send_message(self):
        CalendarSMSSettings.objects.create(
            email=self.email,
            password=self.password,
            website=CalendarSMSWebsites.objects.create(
                site=Site.objects.get(pk=1))
        )
        sendSMS(self.title)
        self.assertEqual(CalendarSMSLogs.objects.all().count(), 1)
        self.assertEqual(CalendarSMSLogs.objects.get(pk=1).title, self.title)
