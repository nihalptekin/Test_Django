# Generated by Django 4.2.4 on 2023-08-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='passenger',
            field=models.ManyToManyField(related_name='reservations', to='flights.passenger'),
        ),
    ]