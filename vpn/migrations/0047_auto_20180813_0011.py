# Generated by Django 2.0.6 on 2018-08-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0046_auto_20180803_0314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subnettosubnet',
            old_name='keyringtries',
            new_name='keyingtries',
        ),
        migrations.RemoveField(
            model_name='subnettosubnet',
            name='also',
        ),
        migrations.AlterField(
            model_name='subnettosubnet',
            name='auto',
            field=models.CharField(blank=True, default='add', help_text='eg. <b><a>start OR add</a></b>', max_length=16),
        ),
        migrations.AlterField(
            model_name='subnettosubnet',
            name='left',
            field=models.CharField(default='Input IP', help_text='Valid - <b><a>Input IP</a></b> OR <b><a>%defaultroute</a></b> OR <b><a>%any</a></b> OR <b><a>%opportunistic</a></b>', max_length=16),
        ),
        migrations.AlterField(
            model_name='subnettosubnet',
            name='leftsubnet',
            field=models.CharField(blank=True, default='0.0.0.0/0', help_text='eg. 0.0.0.0/0', max_length=16),
        ),
        migrations.AlterField(
            model_name='subnettosubnet',
            name='right',
            field=models.CharField(default='Input IP', help_text='Valid - <b><a>Input IP</a></b> OR <b><a>%defaultroute</a></b>', max_length=16),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='auto',
            field=models.CharField(blank=True, default='add', help_text='eg. <b><a>start OR add</a></b>', max_length=16),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='dpdaction',
            field=models.CharField(blank=True, default='clear', help_text='Valid - <b><a>clear</a></b> OR <b><a>restart</a></b> OR <b><a>hold</a></b>', max_length=4),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='dpddelay',
            field=models.CharField(blank=True, default='15', help_text='eg. <b><a>10</a></b>', max_length=4),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='dpdtimeout',
            field=models.CharField(blank=True, default='90', help_text='eg. <b><a>150</a></b>', max_length=4),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='left',
            field=models.CharField(default='Input IP', help_text='Valid - <b><a>Input IP</a></b> OR <b><a>%defaultroute</a></b> OR <b><a>%any</a></b> OR <b><a>%opportunistic</a></b>', max_length=16),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='leftrsasigkey',
            field=models.CharField(blank=True, default='%cert', help_text='eg. <b><a>%cert</a></b>', max_length=16),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='leftsubnet',
            field=models.CharField(blank=True, default='0.0.0.0/0', help_text='eg. 0.0.0.0/0', max_length=16),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='mobike',
            field=models.CharField(blank=True, default='yes', help_text='Valid - <b><a>no</a></b> OR <b><a>yes</a></b>', max_length=3),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='narrowing',
            field=models.CharField(blank=True, default='', help_text='Valid - <b><a>no</a></b> OR <b><a>yes</a></b>', max_length=3),
        ),
        migrations.AlterField(
            model_name='vpnforremotehost',
            name='right',
            field=models.CharField(default='Input IP', help_text='Valid - <b><a>Input IP</a></b> OR <b><a>%defaultroute</a></b> OR <b><a>%any</a></b>', max_length=16),
        ),
    ]