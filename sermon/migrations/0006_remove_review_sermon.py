# Generated by Django 5.1 on 2024-08-26 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sermon', '0005_review_sermon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='sermon',
        ),
    ]
