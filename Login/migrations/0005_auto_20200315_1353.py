# Generated by Django 2.2.6 on 2020-03-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_auto_20200315_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_of_user',
            name='userImg',
            field=models.FileField(default='/static/media/images/avatar/no-ava.png', upload_to=''),
        ),
    ]
