# Generated by Django 2.2.6 on 2019-11-07 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamefitnessweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercises',
            options={},
        ),
        migrations.AlterModelOptions(
            name='games',
            options={},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={},
        ),
        migrations.AlterField(
            model_name='users',
            name='email_address',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='game_id',
            field=models.CharField(choices=[('Tennis', 'tennis'), ('Golf', 'golf'), ('Soccer', 'soccer'), ('Basketball', 'basketball'), ('Baseball', 'baseball'), ('Football', 'football'), ('Badminton', 'badminton'), ('Volleyball', 'volleyball')], max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterModelTable(
            name='exercises',
            table=None,
        ),
        migrations.AlterModelTable(
            name='games',
            table=None,
        ),
        migrations.AlterModelTable(
            name='users',
            table=None,
        ),
    ]