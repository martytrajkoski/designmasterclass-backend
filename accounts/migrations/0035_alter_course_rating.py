# Generated by Django 4.2.6 on 2024-03-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_course_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]