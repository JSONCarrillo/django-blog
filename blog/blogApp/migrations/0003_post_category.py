# Generated by Django 4.0.1 on 2022-01-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[], default='uncategorized', max_length=50),
        ),
    ]
