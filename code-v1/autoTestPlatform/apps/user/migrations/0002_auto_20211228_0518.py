# Generated by Django 2.2 on 2021-12-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='create_time',
            field=models.CharField(default='2021-12-28 05:18:49', max_length=256),
        ),
        migrations.AlterField(
            model_name='image',
            name='update_time',
            field=models.CharField(default='2021-12-28 05:18:49', max_length=256),
        ),
        migrations.AlterField(
            model_name='register',
            name='cellphone',
            field=models.IntegerField(default=20211228051849, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='create_time',
            field=models.CharField(default='2021-12-28 05:18:49', max_length=256),
        ),
        migrations.AlterField(
            model_name='register',
            name='update_time',
            field=models.CharField(default='2021-12-28 05:18:49', max_length=256),
        ),
    ]