# Generated by Django 2.2.6 on 2020-03-15 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_of_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('userImg', models.TextField(default='images/avatar/no-ava.png')),
                ('userStatus', models.TextField(default='New Member')),
            ],
        ),
    ]
