# Generated by Django 4.2.13 on 2024-05-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDataManagement', '0010_matchhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchhistory',
            name='matchtype',
            field=models.CharField(db_column='MatchType', default='', max_length=8),
        ),
    ]
