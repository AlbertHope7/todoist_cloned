# Generated by Django 4.1.7 on 2023-03-13 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todos", "0002_alter_todo_due_until"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="todo_users",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]