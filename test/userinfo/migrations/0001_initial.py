# Generated by Django 3.2.20 on 2023-10-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=500, null=True)),
                ('residence', models.CharField(max_length=500, null=True)),
                ('goal', models.CharField(max_length=100, null=True)),
                ('weight', models.IntegerField(default=40, null=True)),
                ('attendance', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
