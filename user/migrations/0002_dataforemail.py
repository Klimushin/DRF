# Generated by Django 3.2.12 on 2022-02-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataForEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_time', models.FloatField(blank=True, null=True)),
                ('request_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
