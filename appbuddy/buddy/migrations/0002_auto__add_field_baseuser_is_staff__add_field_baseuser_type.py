# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BaseUser.is_staff'
        db.add_column(u'buddy_baseuser', 'is_staff',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BaseUser.type'
        db.add_column(u'buddy_baseuser', 'type',
                      self.gf('django.db.models.fields.TextField')(default='agent', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BaseUser.is_staff'
        db.delete_column(u'buddy_baseuser', 'is_staff')

        # Deleting field 'BaseUser.type'
        db.delete_column(u'buddy_baseuser', 'type')


    models = {
        u'buddy.agentinfo': {
            'Meta': {'object_name': 'AgentInfo', '_ormbases': [u'buddy.BaseUser']},
            'agent_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            u'baseuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['buddy.BaseUser']", 'unique': 'True', 'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mobile_os': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'buddy.appbuddyuser': {
            'Meta': {'object_name': 'AppBuddyUser'},
            'agent_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['buddy.AgentInfo']"}),
            'app_packages': ('django.db.models.fields.TextField', [], {}),
            'app_version': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'device_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['buddy.DeviceInfo']"}),
            'email_address': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imei': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'install_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'location_info': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['buddy.LocationInfo']"}),
            'mac_address': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'os_version': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'buddy.appinfo': {
            'Meta': {'object_name': 'AppInfo'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'app_version': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['buddy.Category']", 'symmetrical': 'False'}),
            'cities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'apps'", 'symmetrical': 'False', 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'download_size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'download_time_3g': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'download_time_edge': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'download_time_wifi': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'min_android_version': ('django.db.models.fields.CharField', [], {'default': '14', 'max_length': '10'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'open_on_install': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'package_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'whitelisted_urls': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'apps'", 'symmetrical': 'False', 'to': u"orm['buddy.WhitelistUrl']"})
        },
        u'buddy.baseuser': {
            'Meta': {'object_name': 'BaseUser'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['buddy.CityInfo']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'type': ('django.db.models.fields.TextField', [], {'default': "'agent'", 'max_length': '10'})
        },
        u'buddy.businesspartner': {
            'Meta': {'object_name': 'BusinessPartner', '_ormbases': [u'buddy.BaseUser']},
            u'baseuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['buddy.BaseUser']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'buddy.category': {
            'Meta': {'object_name': 'Category'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'buddy.cityinfo': {
            'Meta': {'object_name': 'CityInfo'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'buddy.datacardinfo': {
            'Meta': {'object_name': 'DataCardInfo'},
            'card_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'reference_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'buddy.deviceinfo': {
            'Meta': {'object_name': 'DeviceInfo'},
            'box_identifier': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'card_info': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'to': u"orm['buddy.DataCardInfo']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'devices'", 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'device_type': ('django.db.models.fields.CharField', [], {'default': "'tplink'", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mac_address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'buddy.downloadlog': {
            'Meta': {'object_name': 'DownloadLog'},
            'agent_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'downloads'", 'to': u"orm['buddy.DeviceInfo']"}),
            'app_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'downloads'", 'to': u"orm['buddy.AppInfo']"}),
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'device_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'installs'", 'to': u"orm['buddy.DeviceInfo']"}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'downloads'", 'to': u"orm['buddy.LocationInfo']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'operator': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'package_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'installing'", 'max_length': '15'}),
            'user_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'downloads'", 'to': u"orm['buddy.AppBuddyUser']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'buddy.locationinfo': {
            'Meta': {'object_name': 'LocationInfo'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'agent': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'locations'", 'null': 'True', 'default': 'None', 'to': u"orm['buddy.AgentInfo']", 'blank': 'True', 'unique': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'device_info': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'locations'", 'null': 'True', 'default': 'None', 'to': u"orm['buddy.DeviceInfo']", 'blank': 'True', 'unique': 'True'}),
            'foot_fall': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landline_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '12', 'decimal_places': '8', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '12', 'decimal_places': '8', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stores'", 'to': u"orm['buddy.LocationPartner']"}),
            'preferred_days': ('django.db.models.fields.CharField', [], {'default': "'all'", 'max_length': '20'}),
            'preferred_time': ('django.db.models.fields.CharField', [], {'default': "'all'", 'max_length': '20'}),
            'store_manager_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'store_manager_number': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'buddy.locationpartner': {
            'Meta': {'object_name': 'LocationPartner', '_ormbases': [u'buddy.BaseUser']},
            u'baseuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['buddy.BaseUser']", 'unique': 'True', 'primary_key': 'True'}),
            'businessPartner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_partners'", 'to': u"orm['buddy.BusinessPartner']"})
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
        },
        u'buddy.whitelisturl': {
            'Meta': {'object_name': 'WhitelistUrl'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'proxy'", 'max_length': '10'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['buddy']