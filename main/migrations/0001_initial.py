# Generated by Django 3.1.7 on 2021-06-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mainmodule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('task', models.CharField(max_length=100)),
                ('tasktime', models.CharField(max_length=100)),
            ],
        ),
    ]
