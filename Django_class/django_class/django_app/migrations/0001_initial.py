# Generated by Django 3.1.5 on 2021-01-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('gmail', models.EmailField(max_length=100, unique=True)),
                ('Age', models.CharField(max_length=3)),
                ('QUALIFICATON', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=150)),
                ('Blood_group', models.CharField(max_length=150)),
                ('INTERST_AREA', models.CharField(max_length=150)),
                ('INSTAGRAM_ID', models.URLField(max_length=150)),
                ('JOIN_YW', models.TextField()),
                ('EACH_WEEK', models.CharField(max_length=10)),
            ],
        ),
    ]
