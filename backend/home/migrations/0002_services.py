# Generated by Django 2.2.26 on 2022-10-10 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=256)),
                ('createdDate', models.DateField()),
                ('terminatedDate', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]