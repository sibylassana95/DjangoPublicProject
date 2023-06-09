# Generated by Django 4.0.5 on 2022-07-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=150)),
                ('ecole', models.CharField(max_length=150)),
                ('prenom', models.CharField(blank=True, max_length=150, null=True)),
                ('profil', models.ImageField(blank=True, upload_to='images_panel')),
            ],
            options={
                'verbose_name': ('Panel',),
                'verbose_name_plural': 'Panels',
            },
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=150)),
                ('matiere', models.CharField(max_length=150)),
                ('salaire', models.IntegerField(blank=True, null=True)),
                ('profil', models.ImageField(blank=True, upload_to='images_panel')),
            ],
            options={
                'verbose_name': ('Prof',),
                'verbose_name_plural': 'Profs',
            },
        ),
    ]
