# Generated by Django 4.2.11 on 2024-05-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDataManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uIs42',
            field=models.BooleanField(db_column='uIs42', default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='udesc',
            field=models.CharField(db_column='uDesc', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='uemail',
            field=models.CharField(db_column='uEmail', default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='ufname',
            field=models.CharField(db_column='uFName', default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='uip',
            field=models.CharField(db_column='uIp', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='ulname',
            field=models.CharField(db_column='uLName', default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='uprofilebgpic',
            field=models.CharField(db_column='uProfileBgPic', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='uprofilepic',
            field=models.CharField(db_column='uProfilePic', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='uregdate',
            field=models.DateTimeField(db_column='uRegDate', default=''),
        ),
    ]
