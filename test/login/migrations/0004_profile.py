# Generated by Django 3.2.20 on 2023-09-22 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_rename_id_account_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='images/')),
                ('residence', models.CharField(max_length=500)),
            ],
        ),
    ]
