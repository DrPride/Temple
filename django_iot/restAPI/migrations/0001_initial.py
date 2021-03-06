# Generated by Django 2.0.3 on 2018-04-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('led13', models.BooleanField(default=False)),
                ('temperature', models.FloatField(default=True)),
                ('sensors1', models.FloatField(default=True)),
                ('sensors2', models.FloatField(default=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
