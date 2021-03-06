# Generated by Django 4.0.3 on 2022-03-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=10, null=True)),
                ('branche', models.CharField(choices=[('Select', 'Select'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('IT', 'IT'), ('EEE', 'EEE'), ('MECH', 'MECH')], max_length=10, null=True)),
            ],
        ),
    ]
