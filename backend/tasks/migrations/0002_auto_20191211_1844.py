# Generated by Django 2.2.7 on 2019-12-11 18:44

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(default=django.db.models.expressions.F(
                'assignee'), on_delete=django.db.models.deletion.SET_DEFAULT, related_name='tasks_todo', to='profiles.Profile'),
        ),
        migrations.DeleteModel(
            name='Receiver',
        ),
        migrations.DeleteModel(
            name='SomeForeignModel',
        ),
    ]
