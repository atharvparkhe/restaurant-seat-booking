# Generated by Django 3.2.8 on 2021-10-30 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellermodel',
            name='aadhar_card',
        ),
    ]