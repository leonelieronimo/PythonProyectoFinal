# Generated by Django 4.0.5 on 2022-06-25 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('link', models.TextField(blank=True, null=True)),
            ],
        ),
    ]