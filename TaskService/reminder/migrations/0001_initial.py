# Generated by Django 4.0.2 on 2022-04-29 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameTask', models.CharField(max_length=255)),
                ('deadline', models.DateField()),
            ],
        ),
    ]
