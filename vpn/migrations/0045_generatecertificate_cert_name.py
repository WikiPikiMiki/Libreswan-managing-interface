# Generated by Django 2.0.6 on 2018-07-29 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0044_auto_20180722_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatecertificate',
            name='cert_name',
            field=models.CharField(blank=True, default='', help_text='<b><a>System Generated - Do not alter</a></b>', max_length=15),
        ),
    ]
