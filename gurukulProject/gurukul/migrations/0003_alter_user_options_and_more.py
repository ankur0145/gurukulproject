# Generated by Django 4.2.3 on 2023-07-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurukul', '0002_categories_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateField(),
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]