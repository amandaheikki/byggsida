# Generated by Django 4.0.4 on 2022-05-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_contactmodel_rename_aboutpage_aboutmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/%y')),
            ],
        ),
    ]
