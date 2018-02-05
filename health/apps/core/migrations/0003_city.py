# Generated by Django 2.0.2 on 2018-02-04 17:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_states'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=6)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]