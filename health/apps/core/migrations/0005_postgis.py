from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cities'),
    ]

    operations = [
        CreateExtension('postgis'),
    ]
