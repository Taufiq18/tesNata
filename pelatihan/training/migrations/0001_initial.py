# Generated by Django 5.1 on 2024-09-03 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('technical', 'Technical'), ('management', 'Management'), ('soft_skills', 'Soft Skills'), ('other', 'Other')], max_length=20)),
                ('mentor', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
