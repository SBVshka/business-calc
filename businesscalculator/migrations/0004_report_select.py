# Generated by Django 4.2.2 on 2023-07-04 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesscalculator', '0003_alter_balance_options_alter_company_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='select',
            field=models.BooleanField(default=True, verbose_name='Выбор отчета'),
            preserve_default=False,
        ),
    ]
