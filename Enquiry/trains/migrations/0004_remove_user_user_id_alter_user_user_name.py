# Generated by Django 4.0.3 on 2022-07-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
