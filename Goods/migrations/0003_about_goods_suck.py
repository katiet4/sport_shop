# Generated by Django 3.0.2 on 2020-03-14 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_about_goods_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_goods',
            name='suck',
            field=models.TextField(default='fdasf'),
        ),
    ]
