# Generated by Django 4.1.3 on 2022-11-28 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_entrada_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['categoria'], 'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
    ]
