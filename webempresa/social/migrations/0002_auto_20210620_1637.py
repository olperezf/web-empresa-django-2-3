# Generated by Django 3.2.3 on 2021-06-20 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
        migrations.RenameField(
            model_name='link',
            old_name='utl',
            new_name='url',
        ),
    ]
