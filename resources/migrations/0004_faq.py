# Generated by Django 4.0.6 on 2022-08-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=800)),
                ('ans', models.CharField(max_length=1000)),
            ],
        ),
    ]
