# Generated by Django 4.2.3 on 2023-10-02 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_remove_user_info_user_lev_user_info_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='User_ID',
        ),
    ]
