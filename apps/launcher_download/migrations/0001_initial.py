<<<<<<< HEAD
# Generated by Django 4.2.6 on 2023-11-20 18:31
=======
# Generated by Django 4.2.7 on 2023-11-20 17:51
>>>>>>> main

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Launcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='launchers/')),
            ],
        ),
    ]
