# Generated by Django 2.0.6 on 2018-06-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='max_way',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
