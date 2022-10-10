# Generated by Django 4.0.6 on 2022-10-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_alter_event_category_alter_faq_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='show',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='show',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='category',
            field=models.CharField(choices=[('Resource', 'Resources'), ('Internship', 'Internship'), ('none', 'none')], default='none', max_length=50, verbose_name='Cateeegory'),
        ),
    ]
