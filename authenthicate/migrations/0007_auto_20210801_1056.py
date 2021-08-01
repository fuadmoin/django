# Generated by Django 3.2.5 on 2021-08-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenthicate', '0006_remove_cafeprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cafeName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='CafeProfile',
        ),
    ]
