# Generated by Django 3.0.1 on 2019-12-25 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='emali',
            new_name='email',
        ),
    ]
