# Generated by Django 5.1.6 on 2025-02-25 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Emp_id',
            new_name='Emp',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='l_id',
            new_name='l',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='department_id',
            new_name='department',
        ),
    ]
