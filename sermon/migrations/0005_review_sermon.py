# Generated by Django 5.1 on 2024-08-26 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermon', '0004_alter_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='sermon',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sermon.sermon'),
            preserve_default=False,
        ),
    ]
