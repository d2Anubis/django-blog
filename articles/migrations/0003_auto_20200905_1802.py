# Generated by Django 3.1 on 2020-09-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200905_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.CharField(max_length=20),
        ),
    ]
