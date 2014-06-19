# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CityInfo'
        db.create_table(u'buddy_cityinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'buddy', ['CityInfo'])

        # Adding model 'DeviceInfo'
        db.create_table(u'buddy_deviceinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('boxIdentifier', self.gf('django.db.models.fields.IntegerField')()),
            ('deviceType', self.gf('django.db.models.fields.CharField')(default='tplink', max_length=20)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='devices', to=orm['buddy.CityInfo'])),
        ))
        db.send_create_signal(u'buddy', ['DeviceInfo'])

        # Adding model 'PushNotificatonRegistration'
        db.create_table(u'buddy_pushnotificatonregistration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('unique_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('device_type', self.gf('django.db.models.fields.CharField')(default='android', max_length=20)),
            ('registration_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('app_version', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('os_version', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('make', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('imei', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('screen_width', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('screen_height', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'buddy', ['PushNotificatonRegistration'])

        # Adding model 'Category'
        db.create_table(u'buddy_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('where_clause', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'buddy', ['Category'])

        # Adding model 'AppInfo'
        db.create_table(u'buddy_appinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('package_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('market_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('download_time_wifi', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('download_time_3g', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('download_time_edge', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('open_on_install', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('app_version', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('min_android_version', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'buddy', ['AppInfo'])

        # Adding M2M table for field categories on 'AppInfo'
        m2m_table_name = db.shorten_name(u'buddy_appinfo_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('appinfo', models.ForeignKey(orm[u'buddy.appinfo'], null=False)),
            ('category', models.ForeignKey(orm[u'buddy.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['appinfo_id', 'category_id'])

        # Adding model 'AgentInfo'
        db.create_table(u'buddy_agentinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('mobileNumber', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agents', to=orm['buddy.CityInfo'])),
            ('state', self.gf('django.db.models.fields.CharField')(default='Karnataka', max_length=50)),
            ('pinCode', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('agentId', self.gf('django.db.models.fields.PositiveIntegerField')(default=None, null=True, blank=True)),
            ('photograph', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('validatedOn', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'buddy', ['AgentInfo'])

        # Adding model 'LocationPartner'
        db.create_table(u'buddy_locationpartner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('mobileNumber', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='partners', to=orm['buddy.CityInfo'])),
            ('numberOfStores', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'buddy', ['LocationPartner'])

        # Adding model 'LocationInfo'
        db.create_table(u'buddy_locationinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stores', to=orm['buddy.LocationPartner'])),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('footFall', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='locations', to=orm['buddy.CityInfo'])),
            ('landlineNumber', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('storeManagerName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('storeManagerNumber', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('preferredDays', self.gf('django.db.models.fields.CharField')(default='all', max_length=20)),
            ('preferredTime', self.gf('django.db.models.fields.CharField')(default='all', max_length=20)),
            ('deviceInfo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='locations', to=orm['buddy.DeviceInfo'])),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='locations', to=orm['buddy.AgentInfo'])),
        ))
        db.send_create_signal(u'buddy', ['LocationInfo'])

        # Adding model 'AppBuddyUser'
        db.create_table(u'buddy_appbuddyuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('deviceId', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('imei', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('macAddress', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('agentInfo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buddy.AgentInfo'])),
            ('deviceInfo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buddy.DeviceInfo'])),
            ('locationInfo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buddy.LocationInfo'])),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('appVersion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('osVersion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('emailAddress', self.gf(u'django_hstore.fields.DictionaryField')()),
            ('phoneNumber', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('app_packages', self.gf(u'django_hstore.fields.DictionaryField')()),
        ))
        db.send_create_signal(u'buddy', ['AppBuddyUser'])


    def backwards(self, orm):
        # Deleting model 'CityInfo'
        db.delete_table(u'buddy_cityinfo')

        # Deleting model 'DeviceInfo'
        db.delete_table(u'buddy_deviceinfo')

        # Deleting model 'PushNotificatonRegistration'
        db.delete_table(u'buddy_pushnotificatonregistration')

        # Deleting model 'Category'
        db.delete_table(u'buddy_category')

        # Deleting model 'AppInfo'
        db.delete_table(u'buddy_appinfo')

        # Removing M2M table for field categories on 'AppInfo'
        db.delete_table(db.shorten_name(u'buddy_appinfo_categories'))

        # Deleting model 'AgentInfo'
        db.delete_table(u'buddy_agentinfo')

        # Deleting model 'LocationPartner'
        db.delete_table(u'buddy_locationpartner')

        # Deleting model 'LocationInfo'
        db.delete_table(u'buddy_locationinfo')

        # Deleting model 'AppBuddyUser'
        db.delete_table(u'buddy_appbuddyuser')


    models = {
        u'buddy.agentinfo': {
            'Meta': {'object_name': 'AgentInfo'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'agentId': ('django.db.models.fields.PositiveIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agents'", 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobileNumber': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photograph': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pinCode': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'Karnataka'", 'max_length': '50'}),
            'validatedOn': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'buddy.appbuddyuser': {
            'Meta': {'object_name': 'AppBuddyUser'},
            'agentInfo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['buddy.AgentInfo']"}),
            'appVersion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'app_packages': (u'django_hstore.fields.DictionaryField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'deviceId': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'deviceInfo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['buddy.DeviceInfo']"}),
            'emailAddress': (u'django_hstore.fields.DictionaryField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imei': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'locationInfo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['buddy.LocationInfo']"}),
            'macAddress': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'osVersion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        u'buddy.cityinfo': {
            'Meta': {'object_name': 'CityInfo'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'buddy.deviceinfo': {
            'Meta': {'object_name': 'DeviceInfo'},
            'boxIdentifier': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'devices'", 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'deviceType': ('django.db.models.fields.CharField', [], {'default': "'tplink'", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'buddy.locationinfo': {
            'Meta': {'object_name': 'LocationInfo'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['buddy.AgentInfo']"}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'deviceInfo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['buddy.DeviceInfo']"}),
            'footFall': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landlineNumber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stores'", 'to': u"orm['buddy.LocationPartner']"}),
            'preferredDays': ('django.db.models.fields.CharField', [], {'default': "'all'", 'max_length': '20'}),
            'preferredTime': ('django.db.models.fields.CharField', [], {'default': "'all'", 'max_length': '20'}),
            'storeManagerName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'storeManagerNumber': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'buddy.locationpartner': {
            'Meta': {'object_name': 'LocationPartner'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partners'", 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobileNumber': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numberOfStores': ('django.db.models.fields.PositiveIntegerField', [], {})
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