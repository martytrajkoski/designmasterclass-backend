# Generated by Django 4.2.6 on 2024-03-07 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_remove_customuser_courses_remove_customuser_quizzes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuserquizzes',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='customuserquizzes',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.course'),
        ),
        migrations.DeleteModel(
            name='CustomUserCourses',
        ),
        migrations.DeleteModel(
            name='CustomUserQuizzes',
        ),
    ]
