# Generated by Django 4.1.7 on 2023-03-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('contenu', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]