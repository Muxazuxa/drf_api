# Generated by Django 2.0.7 on 2018-07-03 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='descriprion',
            new_name='description',
        ),
    ]
