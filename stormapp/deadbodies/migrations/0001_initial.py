# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DeadBody'
        db.create_table('deadbodies_deadbody', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('nlong', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=15, decimal_places=5, blank=True)),
            ('nlat', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=15, decimal_places=5, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='U', max_length=1)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=150, null=True, blank=True)),
            ('date_reported', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
        ))
        db.send_create_signal('deadbodies', ['DeadBody'])


    def backwards(self, orm):
        # Deleting model 'DeadBody'
        db.delete_table('deadbodies_deadbody')


    models = {
        'deadbodies.deadbody': {
            'Meta': {'object_name': 'DeadBody'},
            'date_reported': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nlat': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'nlong': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'})
        }
    }

    complete_apps = ['deadbodies']