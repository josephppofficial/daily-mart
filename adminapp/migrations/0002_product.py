# Generated by Django 3.2.25 on 2024-06-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(default='', max_length=10)),
                ('price', models.IntegerField()),
                ('category', models.CharField(default='', max_length=10)),
                ('image', models.ImageField(default='null.jpg', upload_to='image')),
            ],
        ),
    ]
