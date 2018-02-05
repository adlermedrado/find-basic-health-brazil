import csv
from django.db import migrations


def add_cities(apps, schema_editor):
    State = apps.get_model('core', 'State')
    City = apps.get_model('core', 'City')
    city_list = csv.DictReader(open('data/cities.csv'))
    for city_info in city_list:
        state = State.objects.filter(code=city_info['CD_GCUF'])
        city = City()
        city.name = city_info['NM_MUN_2016']
        city.slug = city_info['NM_UF_SIGLA']
        city.code = city_info['CD_GCMUN']
        city.state = state[0]
        city.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_city'),
    ]

    operations = [
        migrations.RunPython(add_cities)
    ]
