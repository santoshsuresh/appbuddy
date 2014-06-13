# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PushNotificatonRegistration'
        db.create_table(u'buddy_pushnotificatonregistration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('unique_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('device_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('registration_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('app_version', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('os_version', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('make', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('imei', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('screen_width', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('screen_height', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'buddy', ['PushNotificatonRegistration'])


    def backwards(self, orm):
        # Deleting model 'PushNotificatonRegistration'
        db.delete_table(u'buddy_pushnotificatonregistration')


    models = {
        u'buddy.pushnotificatonregistration': {
            'Meta': {'object_name': 'PushNotificatonRegistration'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'app_version': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'device_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imei': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'os_version': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'registration_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'screen_height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'screen_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['buddy']