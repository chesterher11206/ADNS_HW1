# Generated by Django 2.2 on 2019-04-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20190408_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='photo',
            field=models.CharField(choices=[('ONE', 'images/fox.png'), ('TWO', 'images/dog.png'), ('THREE', 'images/cat.png'), ('FOUR', 'images/rabbit.png'), ('FIVE', 'images/raccoon.png'), ('SIX', 'images/wolf.png')], default='', max_length=50, verbose_name='Photo'),
        ),
    ]
