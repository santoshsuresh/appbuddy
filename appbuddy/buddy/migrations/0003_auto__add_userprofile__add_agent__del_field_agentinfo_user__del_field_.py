# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'buddy_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agents', to=orm['buddy.CityInfo'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='promoter', max_length=10)),
        ))
        db.send_create_signal(u'buddy', ['UserProfile'])

        # Adding model 'Agent'
        db.create_table(u'buddy_agent', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('agent_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'buddy', ['Agent'])

        # Deleting field 'AgentInfo.user'
        db.delete_column(u'buddy_agentinfo', 'user_id')

        # Deleting field 'AgentInfo.city'
        db.delete_column(u'buddy_agentinfo', 'city_id')

        # Deleting field 'AgentInfo.photograph'
        db.delete_column(u'buddy_agentinfo', 'photograph')

        # Deleting field 'AgentInfo.name'
        db.delete_column(u'buddy_agentinfo', 'name')

        # Deleting field 'AgentInfo.mobile_number'
        db.delete_column(u'buddy_agentinfo', 'mobile_number')

        # Deleting field 'AgentInfo.state'
        db.delete_column(u'buddy_agentinfo', 'state')

        # Deleting field 'AgentInfo.address'
        db.delete_column(u'buddy_agentinfo', 'address')

        # Deleting field 'AgentInfo.active'
        db.delete_column(u'buddy_agentinfo', 'active')

        # Deleting field 'AgentInfo.email'
        db.delete_column(u'buddy_agentinfo', 'email')

        # Deleting field 'AgentInfo.validated_on'
        db.delete_column(u'buddy_agentinfo', 'validated_on')

        # Deleting field 'AgentInfo.pin_code'
        db.delete_column(u'buddy_agentinfo', 'pin_code')


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'buddy_userprofile')

        # Deleting model 'Agent'
        db.delete_table(u'buddy_agent')

        # Adding field 'AgentInfo.user'
        db.add_column(u'buddy_agentinfo', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Adding field 'AgentInfo.city'
        db.add_column(u'buddy_agentinfo', 'city',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='agents', to=orm['buddy.CityInfo']),
                      keep_default=False)

        # Adding field 'AgentInfo.photograph'
        db.add_column(u'buddy_agentinfo', 'photograph',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'AgentInfo.name'
        db.add_column(u'buddy_agentinfo', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'AgentInfo.mobile_number'
        db.add_column(u'buddy_agentinfo', 'mobile_number',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=20, unique=True),
                      keep_default=False)

        # Adding field 'AgentInfo.state'
        db.add_column(u'buddy_agentinfo', 'state',
                      self.gf('django.db.models.fields.CharField')(default='Karnataka', max_length=50),
                      keep_default=False)

        # Adding field 'AgentInfo.address'
        db.add_column(u'buddy_agentinfo', 'address',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)

        # Adding field 'AgentInfo.active'
        db.add_column(u'buddy_agentinfo', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'AgentInfo.email'
        db.add_column(u'buddy_agentinfo', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=1, max_length=75, unique=True),
                      keep_default=False)

        # Adding field 'AgentInfo.validated_on'
        db.add_column(u'buddy_agentinfo', 'validated_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'AgentInfo.pin_code'
        db.add_column(u'buddy_agentinfo', 'pin_code',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'buddy.agent': {
            'Meta': {'object_name': 'Agent', '_ormbases': [u'auth.User']},
            'agent_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'buddy.agentinfo': {
            'Meta': {'object_name': 'AgentInfo'},
            'agent_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mobile_os': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'buddy.appbuddyuser': {
            'Meta': {'object_name': 'AppBuddyUser'},
            'agent_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['buddy.AgentInfo']"}),
            'app_packages': (u'django_hstore.fields.DictionaryField', [], {}),
            'app_version': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'device_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['buddy.DeviceInfo']"}),
            'email_address': (u'django_hstore.fields.DictionaryField', [], {}),
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
        u'buddy.businesspartner': {
            'Meta': {'object_name': 'BusinessPartner'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'business_partners'", 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'Meta': {'object_name': 'LocationPartner'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'businessPartner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_partners'", 'to': u"orm['buddy.BusinessPartner']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partners'", 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_of_stores': ('django.db.models.fields.PositiveIntegerField', [], {})
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
        u'buddy.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agents'", 'to': u"orm['buddy.CityInfo']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'promoter'", 'max_length': '10'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'buddy.whitelisturl': {
            'Meta': {'object_name': 'WhitelistUrl'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'proxy'", 'max_length': '10'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['buddy']