# Generated by Django 2.2.2 on 2019-06-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_student', models.IntegerField(max_length=100)),
                ('id_instructor', models.IntegerField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('lieu', models.CharField(max_length=100)),
            ],
        ),
    ]
