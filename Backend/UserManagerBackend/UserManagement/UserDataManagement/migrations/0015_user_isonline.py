# Generated by Django 4.2.13 on 2024-06-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDataManagement', '0014_user_twofactor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isOnline',
            field=models.BooleanField(db_column='online', default=False),
        ),
    ]
