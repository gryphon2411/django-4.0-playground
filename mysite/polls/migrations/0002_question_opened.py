# Generated by Django 4.1 on 2022-08-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='opened',
            field=models.BooleanField(default=True),
        ),
    ]
