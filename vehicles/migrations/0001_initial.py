# Generated by Django 3.2.16 on 2022-12-16 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=100, null=True)),
                ('fuel_type', models.CharField(choices=[('diesel', 'diesel'), ('petrol', 'petrol'), ('cng', 'cng'), ('ev', 'ev')], default='petrol', max_length=200)),
                ('pyear', models.DateField(null=True)),
                ('runningkm', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]
