# Generated by Django 4.0.4 on 2023-01-24 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_remove_referencemodel_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutmodel',
            name='box2Des',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='box2Title',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='box2_img',
        ),
    ]
