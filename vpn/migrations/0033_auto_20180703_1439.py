# Generated by Django 2.0.6 on 2018-07-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0032_auto_20180703_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaterootcertificate',
            name='cert_password',
            field=models.CharField(blank=True, default='', help_text='<b><a>Enter the Certificate password</a></b>', max_length=20),
        ),
    ]
