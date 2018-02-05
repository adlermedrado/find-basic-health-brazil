import csv
from django.db import migrations


def add_states(apps, schema_editor):
    State = apps.get_model('core', 'State')
    states_list = csv.DictReader(open("data/states.csv"))
    for state_info in states_list:
        state = State()
        state.name = state_info['NM_UF']
        state.slug = state_info['NM_UF_SIGLA']
        state.code = state_info['CD_GCUF']
        state.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_states)
    ]
