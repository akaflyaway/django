# Generated by Django 4.1.3 on 2022-12-05 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
