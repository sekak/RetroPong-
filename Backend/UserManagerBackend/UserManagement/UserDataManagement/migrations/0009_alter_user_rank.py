# Generated by Django 4.2.13 on 2024-05-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDataManagement', '0008_alter_user_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.IntegerField(db_column='Rank', default=1),
        ),
    ]
