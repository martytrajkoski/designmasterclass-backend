# Generated by Django 4.2.6 on 2024-03-20 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_course_stripe_price_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
