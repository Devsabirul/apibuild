# Generated by Django 4.2.5 on 2023-10-08 10:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_garrettcarrillo_delete_malachipollard'),
    ]

    operations = [
        migrations.CreateModel(
            name='PalomaWiley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driscollwhite', models.CharField(max_length=34)),
                ('igorrodriguez', models.EmailField(blank=True, max_length=5, unique=True)),
                ('joelleguerrero', models.IntegerField()),
                ('nerogay', models.BooleanField(blank=True, default=True)),
                ('russellwiggins', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
    ]
