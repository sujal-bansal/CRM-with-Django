# Generated by Django 5.1 on 2024-08-27 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_category_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]
