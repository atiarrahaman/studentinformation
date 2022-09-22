# Generated by Django 3.2.7 on 2021-09-12 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_students_info_student_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_info',
            name='distic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.distic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students_info',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.student_class'),
        ),
    ]