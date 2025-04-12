# Generated by Django 4.2.2 on 2023-07-09 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("businesscalculator", "0007_alter_report_select"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="report",
            name="select",
            field=models.BooleanField(
                choices=[(True, "Баланс"), (False, "ОФР")],
                default=True,
                max_length=15,
                verbose_name="Выбор отчета",
            ),
        ),
    ]
