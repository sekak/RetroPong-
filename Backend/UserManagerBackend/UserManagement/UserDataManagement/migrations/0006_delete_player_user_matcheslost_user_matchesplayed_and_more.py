# Generated by Django 4.2.13 on 2024-05-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDataManagement', '0005_remove_player_pmatcheslost_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.AddField(
            model_name='user',
            name='matcheslost',
            field=models.IntegerField(db_column='MatchesLost', default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='matchesplayed',
            field=models.IntegerField(db_column='MatchesPlayed', default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='matcheswon',
            field=models.IntegerField(db_column='MatchesWon', default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.IntegerField(db_column='Level', default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='xp',
            field=models.IntegerField(db_column='XP', default=0),
        ),
    ]
