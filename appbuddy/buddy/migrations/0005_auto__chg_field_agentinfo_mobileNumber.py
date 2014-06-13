# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AgentInfo.mobileNumber'
        db.alter_column(u'buddy_agentinfo', 'mobileNumber', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

    def backwards(self, orm):

        # Changing field 'AgentInfo.mobileNumber'
        db.alter_column(u'buddy_agentinfo', 'mobileNumber', self.gf('django.db.models.fields.TextField')(unique=True))

    models = {
        u'buddy.agentinfo': {
            'Meta': {'object_name': 'AgentInfo'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'agentId': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobileNumber': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photograph': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pinCode': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'Karnataka'", 'max_length': '50'}),
            'validatedOn': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'buddy.appinfo': {
            'Meta': {'object_name': 'AppInfo'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'app_version': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['buddy.Category']", 'symmetrical': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'download_time_3g': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'download_time_edge': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'download_time_wifi': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'min_android_version': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'open_on_install': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'package_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'buddy.category': {
            'Meta': {'object_name': 'Category'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'where_clause': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'buddy.pushnotificatonregistration': {
            'Meta': {'object_name': 'PushNotificatonRegistration'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'app_version': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'device_type': ('django.db.models.fields.CharField', [], {'default': "'android'", 'max_length': '20'}),
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