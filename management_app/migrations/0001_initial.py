# Generated by Django 5.0.6 on 2024-05-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('creation_by', models.TextField()),
                ('updation_date', models.DateTimeField(auto_now=True, null=True)),
                ('updation_by', models.TextField(blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'pm_product',
                'ordering': ('-creation_date',),
            },
        ),
    ]