from django.db import models
from django.contrib.sites.models import Site

Site.add_to_class(
	'sms_user', models.CharField('Google account',
		blank=True, null=True, max_length = 250)
)
Site.add_to_class(
	'sms_password', models.CharField('Account password',
		blank=True, null=True, max_length = 250)
)
Site.add_to_class(
	'sms_calendar', models.CharField('Calendar ID',
		help_text='For example: fafgttkq8ed2idfgfhdfidn6eok@group.calendar.google.com. \
				You can view the calendar settings - details specific \
					calendar field "Calendar Address" and right there in the brackets.',
		blank=True, null=True, max_length = 250)
)
Site.add_to_class(
	'sms_starttime', models.PositiveIntegerField('Event starts',
		help_text='Specifies how long the event will begin (in seconds)',
		default=120, max_length = 3)
)
Site.add_to_class(
	'sms_endtime', models.PositiveIntegerField('End of event',
		help_text='Specifies how long the event will be complete (in seconds)',
		default=180, max_length = 3)
)
Site.add_to_class(
	'sms_remindertime', models.PositiveIntegerField('Reminder time',
		help_text='Reminder time in minutes',
		default=1, max_length = 2)
)
Site.add_to_class(
	'sms_attempt', models.PositiveIntegerField('Numbers of attempts',
		help_text='Max number of attempts to establish a new memo to the calendar',
		default=11, max_length = 2)
)
Site.add_to_class(
	'sms_delay', models.PositiveIntegerField('Delays',
		help_text='Waiting time between attempts',
		default=5, max_length = 1)
)
