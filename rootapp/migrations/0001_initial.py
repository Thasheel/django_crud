# Generated by Django 5.0.7 on 2024-08-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LifeInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('plans', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('duration', models.CharField(choices=[('3 years', '3 year'), ('5 years', '5 year'), ('10 years', '10 year')], max_length=25)),
            ],
        ),
    ]
