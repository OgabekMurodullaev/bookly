# Generated by Django 5.1.3 on 2024-12-02 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookstatus',
            options={'verbose_name': 'Book status', 'verbose_name_plural': 'Book statuses'},
        ),
    ]
