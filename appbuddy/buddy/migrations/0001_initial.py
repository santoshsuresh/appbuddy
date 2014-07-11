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

        # Adding model 'DataCardInfo'
        db.create_table(u'buddy_datacardinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('card_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('reference_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal(u'buddy', ['DataCardInfo'])

        # Adding model 'DeviceInfo'
        db.create_table(u'buddy_deviceinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('box_identifier', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('device_type', self.gf('django.db.models.fields.CharField')(default='tplink', max_length=20)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='devices', to=orm['buddy.CityInfo'])),
            ('mac_address', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('card_info', self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['buddy.DataCardInfo'], unique=True, null=True, blank=True)),
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
        ))
        db.send_create_signal(u'buddy', ['Category'])

        # Adding model 'WhitelistUrl'
        db.create_table(u'buddy_whitelisturl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(default='proxy', max_length=10)),
        ))
        db.send_create_signal(u'buddy', ['WhitelistUrl'])

        # Adding model 'AppInfo'
        db.create_table(u'buddy_appinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('package_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('market_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('download_time_wifi', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('download_time_3g', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('download_time_edge', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('open_on_install', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('app_version', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('min_android_version', self.gf('django.db.models.fields.CharField')(default=14, max_length=10)),
            ('download_size', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
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

        # Adding M2M table for field cities on 'AppInfo'
        m2m_table_name = db.shorten_name(u'buddy_appinfo_cities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('appinfo', models.ForeignKey(orm[u'buddy.appinfo'], null=False)),
            ('cityinfo', models.ForeignKey(orm[u'buddy.cityinfo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['appinfo_id', 'cityinfo_id'])

        # Adding M2M table for field whitelisted_urls on 'AppInfo'
        m2m_table_name = db.shorten_name(u'buddy_appinfo_whitelisted_urls')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('appinfo', models.ForeignKey(orm[u'buddy.appinfo'], null=False)),
            ('whitelisturl', models.ForeignKey(orm[u'buddy.whitelisturl'], null=False))
        ))
        db.create_unique(m2m_table_name, ['appinfo_id', 'whitelisturl_id'])

        # Adding model 'BaseUser'
        db.create_table(u'buddy_baseuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['buddy.CityInfo'])),
            ('description', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'buddy', ['BaseUser'])

        # Adding model 'AgentInfo'
        db.create_table(u'buddy_agentinfo', (
            (u'baseuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['buddy.BaseUser'], unique=True, primary_key=True)),
            ('agent_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('mobile_os', self.gf('django.db.models.fields.CharField')(default=None, max_length=20, null=True, blank=True)),
            ('make', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'buddy', ['AgentInfo'])

        # Adding model 'BusinessPartner'
        db.create_table(u'buddy_businesspartner', (
            (u'baseuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['buddy.BaseUser'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'buddy', ['BusinessPartner'])

        # Adding model 'LocationPartner'
        db.create_table(u'buddy_locationpartner', (
            (u'baseuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['buddy.BaseUser'], unique=True, primary_key=True)),
            ('businessPartner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_partners', to=orm['buddy.BusinessPartner'])),
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
            ('foot_fall', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='locations', to=orm['buddy.CityInfo'])),
            ('landline_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('store_manager_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('store_manager_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('preferred_days', self.gf('django.db.models.fields.CharField')(default='all', max_length=20)),
            ('preferred_time', self.gf('django.db.models.fields.CharField')(default='all', max_length=20)),
            ('device_info', self.gf('django.db.models.fields.related.OneToOneField')(related_name='locations', null=True, default=None, to=orm['buddy.DeviceInfo'], blank=True, unique=True)),
            ('agent', self.gf('django.db.models.fields.related.OneToOneField')(related_name='locations', null=True, default=None, to=orm['buddy.AgentInfo'], blank=True, unique=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(default=None, null=True, max_digits=12, decimal_places=8, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(default=None, null=True, max_digits=12, decimal_places=8, blank=True)),
        ))
        db.send_create_signal(u'buddy', ['LocationInfo'])

        # Adding model 'AppBuddyUser'
        db.create_table(u'buddy_appbuddyuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('device_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('imei', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('mac_address', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('agent_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buddy.AgentInfo'])),
            ('device_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buddy.DeviceInfo'])),
            ('location_info', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['buddy.LocationInfo'])),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('app_version', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('os_version', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email_address', self.gf('django.db.models.fields.TextField')()),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('app_packages', self.gf('django.db.models.fields.TextField')()),
            ('install_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'buddy', ['AppBuddyUser'])

        # Adding model 'DownloadLog'
        db.create_table(u'buddy_downloadlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user_info', self.gf('django.db.models.fields.related.ForeignKey')(related_name='downloads', to=orm['buddy.AppBuddyUser'])),
            ('device_info', self.gf('django.db.models.fields.related.ForeignKey')(related_name='installs', to=orm['buddy.DeviceInfo'])),
            ('agent_info', self.gf('django.db.models.fields.related.ForeignKey')(related_name='downloads', to=orm['buddy.DeviceInfo'])),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('location_info', self.gf('django.db.models.fields.related.ForeignKey')(related_name='downloads', to=orm['buddy.LocationInfo'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('app_info', self.gf('django.db.models.fields.related.ForeignKey')(related_name='downloads', to=orm['buddy.AppInfo'])),
            ('app_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('package_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.CharField')(default='installing', max_length=15)),
            ('operator', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'buddy', ['DownloadLog'])


    def backwards(self, orm):
        # Deleting model 'CityInfo'
        db.delete_table(u'buddy_cityinfo')

        # Deleting model 'DataCardInfo'
        db.delete_table(u'buddy_datacardinfo')

        # Deleting model 'DeviceInfo'
        db.delete_table(u'buddy_deviceinfo')

        # Deleting model 'PushNotificatonRegistration'
        db.delete_table(u'buddy_pushnotificatonregistration')

        # Deleting model 'Category'
        db.delete_table(u'buddy_category')

        # Deleting model 'WhitelistUrl'
        db.delete_table(u'buddy_whitelisturl')

        # Deleting model 'AppInfo'
        db.delete_table(u'buddy_appinfo')

        # Removing M2M table for field categories on 'AppInfo'
        db.delete_table(db.shorten_name(u'buddy_appinfo_categories'))

        # Removing M2M table for field cities on 'AppInfo'
        db.delete_table(db.shorten_name(u'buddy_appinfo_cities'))

        # Removing M2M table for field whitelisted_urls on 'AppInfo'
        db.delete_table(db.shorten_name(u'buddy_appinfo_whitelisted_urls'))

        # Deleting model 'BaseUser'
        db.delete_table(u'buddy_baseuser')

        # Deleting model 'AgentInfo'
        db.delete_table(u'buddy_agentinfo')

        # Deleting model 'BusinessPartner'
        db.delete_table(u'buddy_businesspartner')

        # Deleting model 'LocationPartner'
        db.delete_table(u'buddy_locationpartner')

        # Deleting model 'LocationInfo'
        db.delete_table(u'buddy_locationinfo')

        # Deleting model 'AppBuddyUser'
        db.delete_table(u'buddy_appbuddyuser')

        # Deleting model 'DownloadLog'
        db.delete_table(u'buddy_downloadlog')


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
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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