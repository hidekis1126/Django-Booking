# Generated by Django 3.1.4 on 2022-02-20 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220221_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='Image',
            new_name='image',
        ),
    ]
