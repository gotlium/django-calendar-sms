# -*- coding: utf-8 -*-

from time import strftime, gmtime, time, sleep
from gdata.calendar.service import gdata, atom, CalendarService

from django.forms.models import model_to_dict
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist

from models import CalendarSMSSettings, CalendarSMSLogs


class DjangoCalendarSMS(object):

    def __init__(self):

        self.account = None
        self.email = None
        self.password = None
        self.calendar = None
        self.start_time = None
        self.end_time = None
        self.reminder_time = None
        self.attempts = None
        self.delays = None

        self.default_cal = '/calendar/feeds/default/private/full'
        self.user_cal = 'https://www.google.com/calendar/feeds/%s/private/full'

        self.agent = 'Google-Calendar_SMS-2.2'
        self.debug = False

    def __message(self, msg):
        if self.debug:
            print(msg)

    def _insertEvent(self):
        event = gdata.calendar.CalendarEventEntry()
        event.title = atom.Title(text=self.title)
        event.content = atom.Content(text=self.content)
        event.where.append(gdata.calendar.Where(value_string=self.where))
        start_time = strftime(
            '%Y-%m-%dT%H:%M:%S.000Z', gmtime(time() + self.start_time)
        )
        end_time = strftime(
            '%Y-%m-%dT%H:%M:%S.000Z', gmtime(time() + self.end_time)
        )
        event.when.append(gdata.calendar.When(
            start_time=start_time, end_time=end_time
        ))
        if not self.calendar:
            new_event = self.cal_client.InsertEvent(event, self.default_cal)
        else:
            new_event = self.cal_client.InsertEvent(
                event, self.user_cal % self.calendar)
        self.edit_link = new_event.GetEditLink().href
        return new_event

    def _addReminder(self, event):
        for a_when in event.when:
            if len(a_when.reminder) > 0:
                a_when.reminder[0].minutes = self.reminder_time
            else:
                a_when.reminder.append(
                    gdata.calendar.Reminder(minutes=self.reminder_time)
                )
        for a_when in event.when:
            if len(a_when.reminder) > 0:
                a_when.reminder[0].method = 'sms'
            else:
                a_when.reminder.append(gdata.calendar.Reminder(method='sms'))
        return self.cal_client.UpdateEvent(event.GetEditLink().href, event)

    def __remove(self):
        try:
            self.cal_client.DeleteEvent(self.edit_link)
        except Exception, msg:
            self.__message(msg)

    def __add(self):
        self.cal_client = CalendarService(
            self.email, self.password, self.agent
        )
        self.cal_client.ProgrammaticLogin()
        self._addReminder(self._insertEvent())

    def __save(self, status):
        CalendarSMSLogs.objects.create(
            title=self.title, email=self.account,
            content=self.content, status=status)

    def __send(self):
        for i in range(self.attempts):
            try:
                self.__message('Sending sms to %s' % self.email)
                self.__add()
                self.__save(True)
                self.__message('successfully')
                break
            except Exception, msg:
                if self.attempts == (i + 1):
                    self.__save(False)
                self.__remove()
                self.__message(msg)
            sleep(self.delays)
            del self.cal_client
            self.__message('attempt %d' % (i + 1))

    def __run(self):
        for self.account in self.accounts:
            self.__dict__.update(model_to_dict(self.account))
            if self.email and self.password:
                self.__send()

    def __get_accounts(self):
        self.accounts = CalendarSMSSettings.objects.filter(
            website__site=Site.objects.get_current(),
            website__status=True,
            status=True
        )
        return self.accounts.exists()

    def send(self, title='', content='', where=''):
        self.title = title
        self.content = content
        self.where = where

        if self.__get_accounts() and title:
            self.__run()
        elif self.debug:
            self.__message('Active accounts not found!')
        else:
            raise ObjectDoesNotExist('Accounts not installed.')


def sendSMS(*args, **kwargs):
    sms = DjangoCalendarSMS()
    sms.send(*args, **kwargs)
