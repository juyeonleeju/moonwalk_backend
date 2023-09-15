# Generated by Django 4.2.3 on 2023-09-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COURS_LEVEL_NM', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'Reward',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='reward',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='reward',
            name='fuel',
        ),
        migrations.RemoveField(
            model_name='reward',
            name='name',
        ),
        migrations.AddField(
            model_name='reward',
            name='COURS_LEVEL_NM',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='reward',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]
