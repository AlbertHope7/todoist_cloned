# Generated by Django 4.1.7 on 2023-03-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="due_until",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
