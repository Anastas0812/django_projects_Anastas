# Generated by Django 5.1.5 on 2025-01-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teachers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
