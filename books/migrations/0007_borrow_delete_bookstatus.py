# Generated by Django 5.1.3 on 2024-12-15 16:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_bookreview_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('borrowed', 'Borrowed'), ('returned', 'Returned'), ('overdue', 'Overdue')], default='borrowed', max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BookStatus',
        ),
    ]
