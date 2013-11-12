# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CalendarSMSWebsites'
        db.create_table('calendar_sms_websites', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, db_index=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site'])),
        ))
        db.send_create_signal(u'calendar_sms', ['CalendarSMSWebsites'])

        # Adding model 'CalendarSMSSettings'
        db.create_table('calendar_sms_settings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, db_index=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('calendar', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.PositiveIntegerField')(default=120, max_length=3)),
            ('end_time', self.gf('django.db.models.fields.PositiveIntegerField')(default=180, max_length=3)),
            ('reminder_time', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, max_length=2)),
            ('attempts', self.gf('django.db.models.fields.PositiveIntegerField')(default=2, max_length=2)),
            ('delays', self.gf('django.db.models.fields.PositiveIntegerField')(default=5, max_length=1)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calendar_sms.CalendarSMSWebsites'])),
        ))
        db.send_create_signal(u'calendar_sms', ['CalendarSMSSettings'])

        # Adding model 'CalendarSMSLogs'
        db.create_table('calendar_sms_logs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, db_index=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calendar_sms.CalendarSMSSettings'])),
        ))
        db.send_create_signal(u'calendar_sms', ['CalendarSMSLogs'])


    def backwards(self, orm):
        # Deleting model 'CalendarSMSWebsites'
        db.delete_table('calendar_sms_websites')

        # Deleting model 'CalendarSMSSettings'
        db.delete_table('calendar_sms_settings')

        # Deleting model 'CalendarSMSLogs'
        db.delete_table('calendar_sms_logs')


    models = {
        u'calendar_sms.calendarsmslogs': {
            'Meta': {'ordering': "['-created']", 'object_name': 'CalendarSMSLogs', 'db_table': "'calendar_sms_logs'"},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calendar_sms.CalendarSMSSettings']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        u'calendar_sms.calendarsmssettings': {
            'Meta': {'object_name': 'CalendarSMSSettings', 'db_table': "'calendar_sms_settings'"},
            'attempts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2', 'max_length': '2'}),
            'calendar': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'delays': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5', 'max_length': '1'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'end_time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '180', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'reminder_time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '2'}),
            'start_time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '120', 'max_length': '3'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calendar_sms.CalendarSMSWebsites']"})
        },
        u'calendar_sms.calendarsmswebsites': {
            'Meta': {'object_name': 'CalendarSMSWebsites', 'db_table': "'calendar_sms_websites'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['calendar_sms']