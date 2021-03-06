# Generated by Django 2.0.6 on 2018-06-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0026_certificateconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificateconfiguration',
            name='expiration_period',
            field=models.IntegerField(default='365', help_text='Certificate Expiration period in days', max_length=4),
        ),
        migrations.AlterField(
            model_name='certificateconfiguration',
            name='common_name',
            field=models.CharField(default='username', help_text="Enter Common Name (eg, your name or your server's hostname)", max_length=20),
        ),
    ]
