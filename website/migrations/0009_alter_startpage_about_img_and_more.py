# Generated by Django 4.0.4 on 2022-05-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_startpage_about_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startpage',
            name='about_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='startpage',
            name='contact_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='startpage',
            name='services_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]