# Generated by Django 4.0.3 on 2022-08-06 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0004_remove_user_user_id_alter_user_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='train_stations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_1', models.CharField(max_length=50)),
                ('station_2', models.CharField(max_length=50)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trains.train')),
            ],
        ),
    ]
