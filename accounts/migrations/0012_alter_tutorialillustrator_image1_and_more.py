# Generated by Django 4.2.6 on 2023-10-19 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_tutorialillustrator_tutorialphotoshop_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialillustrator',
            name='image1',
            field=models.ImageField(blank=True, upload_to='./static/tutorialIllustrator'),
        ),
        migrations.AlterField(
            model_name='tutorialphotoshop',
            name='image1',
            field=models.ImageField(blank=True, upload_to='./static/tutorial/'),
        ),
    ]
