# Generated by Django 5.0.6 on 2024-05-15 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0003_campaign_budget_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="budgetallocation",
            name="budget_amount",
        ),
    ]
