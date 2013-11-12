# -*- coding: utf-8 -*-

from celery.task import Task

from .sms import sendSMS


class SMSSend(Task):
    def run(self, *args, **kwargs):
        sendSMS(*args, **kwargs)
