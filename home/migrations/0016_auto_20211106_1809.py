# Generated by Django 3.2.5 on 2021-11-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20211106_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
