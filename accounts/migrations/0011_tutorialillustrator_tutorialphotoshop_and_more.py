# Generated by Django 4.2.5 on 2023-10-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_tutorial_content1_alter_tutorial_content2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialIllustrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('content1', models.TextField(blank=True)),
                ('content2', models.TextField(blank=True)),
                ('content3', models.TextField(blank=True)),
                ('content4', models.TextField(blank=True)),
                ('content5', models.TextField(blank=True)),
                ('image1', models.ImageField(blank=True, upload_to='./static/tutorial')),
                ('image2', models.ImageField(blank=True, upload_to='./static/tutorial')),
                ('image3', models.ImageField(blank=True, upload_to='./static/tutorial')),
                ('image4', models.ImageField(blank=True, upload_to='./static/tutorial')),
                ('image5', models.ImageField(blank=True, upload_to='./static/tutorial')),
            ],
        ),
        migrations.CreateModel(
            name='TutorialPhotoshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('content1', models.TextField(blank=True)),
                ('content2', models.TextField(blank=True)),
                ('content3', models.TextField(blank=True)),
                ('content4', models.TextField(blank=True)),
                ('content5', models.TextField(blank=True)),
                ('image1', models.ImageField(blank=True, upload_to='./static/tutorial')),
                ('image2', models.ImageField(blank=True, upload_to='./static/tutorial')),
                ('image3', models.ImageField(blank=True, upload_to='./static/tutorial')),
                ('image4', models.ImageField(blank=True, upload_to='./static/tutorial')),
                ('image5', models.ImageField(blank=True, upload_to='./static/tutorial')),
            ],
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
