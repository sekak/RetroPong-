# Generated by Django 4.2.13 on 2024-05-27 10:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cName', models.CharField(db_column='cName', default='', max_length=50)),
                ('cMembers', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), db_column='cMembers', default=list, size=None)),
                ('cImage', models.CharField(db_column='cImage', default='', max_length=100)),
                ('cDesc', models.CharField(db_column='cDesc', default='', max_length=100)),
                ('cAdmin', models.IntegerField(db_column='cAdmin', default=0)),
                ('cCreated', models.DateTimeField(auto_now_add=True, db_column='cCreated')),
                ('cUpdated', models.DateTimeField(auto_now=True, db_column='cUpdated')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mContent', models.TextField(db_column='mContent', default='')),
                ('mSender', models.IntegerField(db_column='mSender', default=0)),
                ('mReceiver', models.IntegerField(db_column='mReceiver', default=0)),
                ('mConversation', models.IntegerField(db_column='mConversation', default=0)),
                ('mCreated', models.DateTimeField(auto_now_add=True, db_column='mCreated')),
                ('mUpdated', models.DateTimeField(auto_now=True, db_column='mUpdated')),
                ('mRead', models.BooleanField(db_column='mRead', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uUsername', models.CharField(db_column='uUsername', default='', max_length=50, unique=True)),
                ('uEmail', models.CharField(db_column='uEmail', default='', max_length=64)),
                ('uFname', models.CharField(db_column='uFName', default='', max_length=64)),
                ('uLname', models.CharField(db_column='uLName', default='', max_length=64)),
                ('AFriends', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), db_column='AFriends', default=list, size=None)),
                ('ARequests', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), db_column='ARequests', default=list, size=None)),
                ('ABlocked', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), db_column='ABlocked', default=list, size=None)),
                ('ABlockedBy', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), db_column='ABlockedBy', default=list, size=None)),
                ('uprofilepic', models.CharField(db_column='uProfilePic', default='', max_length=100)),
                ('uprofilebgpic', models.CharField(db_column='uProfileBgPic', default='', max_length=100)),
                ('udesc', models.CharField(db_column='uDesc', default='', max_length=100)),
            ],
            options={
                'db_table': 'UserDataManagement_user',
                'managed': True,
            },
        ),
    ]
