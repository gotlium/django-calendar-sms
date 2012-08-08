# -*- coding: utf-8 -*-

from time import strftime, gmtime, time, sleep
from django.forms.models import model_to_dict
from django.contrib.sites.models import Site
from gdata.calendar.service import *

class DjangoCalendarSMS(object):

	def __init__(self):
		self.__dict__.update(model_to_dict(
			Site.objects.get_current()
		))
		self.canSend = False
		if self.sms_user and self.sms_password:
			self.canSend = True

	def _insertEvent(self, title = '', content = '', where = ''):
		event = gdata.calendar.CalendarEventEntry()
		event.title = atom.Title(text=title)
		event.content = atom.Content(text=content)
		event.where.append(gdata.calendar.Where(value_string=where))
		start_time = strftime(
			'%Y-%m-%dT%H:%M:%S.000Z', gmtime(time() + self.sms_starttime)
		)
		end_time = strftime(
			'%Y-%m-%dT%H:%M:%S.000Z', gmtime(time() + self.sms_endtime)
		)
		event.when.append(gdata.calendar.When(
			start_time=start_time, end_time=end_time
		))
		if not self.sms_calendar:
			new_event = self.cal_client.InsertEvent(
				event, '/calendar/feeds/default/private/full'
			)
		else:
			new_event = self.cal_client.InsertEvent(event,
				'https://www.google.com/calendar/feeds/%s/private/full' %\
				self.sms_calendar)
		return new_event

	def _addReminder(self, event):
		for a_when in event.when:
			if len(a_when.reminder) > 0:
				a_when.reminder[0].minutes = self.sms_remindertime
			else:
				a_when.reminder.append(
					gdata.calendar.Reminder(minutes=self.sms_remindertime)
				)
		for a_when in event.when:
			if len(a_when.reminder) > 0:
				a_when.reminder[0].method = 'sms'
			else:
				a_when.reminder.append(gdata.calendar.Reminder(method='sms'))
		return self.cal_client.UpdateEvent(event.GetEditLink().href, event)

	def send(self,text_message = '', text_title = '', where = ''):
		if not self.canSend:
			return False
		cnt = 0
		while cnt < self.sms_attempt:
			try:
				self.cal_client = CalendarService(
					self.sms_user, self.sms_password,
					'Google-Calendar_SMS-2.2'
				)
				self.cal_client.ProgrammaticLogin()
				see = self._insertEvent(
					text_title, text_message, where
				)
				self._addReminder(see)
				return True
			except Exception:
				try:
					self.cal_client.DeleteEvent(see.GetEditLink().href)
				except Exception:
					pass
				cnt += 1
			sleep(self.sms_delay)
		return False

def sendSMS(title, text='', where=''):
	sms = DjangoCalendarSMS()
	return sms.send(text, title, where)
