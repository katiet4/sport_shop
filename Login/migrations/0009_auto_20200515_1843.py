# Generated by Django 3.0.6 on 2020-05-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0008_auto_20200515_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_of_user',
            name='userImg',
            field=models.ImageField(default='/static/media/images/avatar/no-ava.png', upload_to='static/media/images/avatar'),
        ),
    ]
