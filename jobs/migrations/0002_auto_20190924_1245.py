# Generated by Django 2.2.2 on 2019-09-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='Project', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(max_length=200),
        ),
    ]
