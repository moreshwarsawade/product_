# Generated by Django 4.1.1 on 2023-02-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
