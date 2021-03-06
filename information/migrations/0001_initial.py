# Generated by Django 3.2.2 on 2021-06-28 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application_of_Moving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_point', models.CharField(max_length=100)),
                ('departure_floor', models.IntegerField()),
                ('destination_point', models.CharField(max_length=100)),
                ('destination_floor', models.IntegerField()),
                ('moving_date', models.DateField()),
                ('storaging_moving', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'application_of_moving',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='Company_Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='information.car')),
            ],
            options={
                'db_table': 'company_car',
            },
        ),
        migrations.CreateModel(
            name='CustomerInfomation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('phone_number', models.CharField(max_length=50)),
                ('terms_of_use', models.BooleanField(default=False)),
                ('personal_information', models.BooleanField(default=False)),
                ('marketing_information', models.BooleanField(default=False)),
                ('customer_registration_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'customer_information',
            },
        ),
        migrations.CreateModel(
            name='Moving_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'moving_type',
            },
        ),
        migrations.CreateModel(
            name='Satisfaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'satisfaction',
            },
        ),
        migrations.CreateModel(
            name='Moving_Company_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('master', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('business_number', models.CharField(max_length=20)),
                ('business_registration_date', models.DateField(auto_now_add=True)),
                ('staff', models.IntegerField()),
                ('matching', models.BooleanField(default=False)),
                ('number_of_car', models.ManyToManyField(related_name='number_of_car', through='information.Company_Car', to='information.Car')),
            ],
            options={
                'db_table': 'company_information',
            },
        ),
        migrations.CreateModel(
            name='Customer_Feedback_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_information', models.BooleanField(default=False)),
                ('revisit', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('feeadback_date', models.DateField(auto_now_add=True)),
                ('feedback', models.TextField()),
                ('company_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_information', to='information.moving_company_information')),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='information', to='information.application_of_moving')),
                ('kindness_satisfaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Kindnedd_satisfaction', to='information.satisfaction')),
                ('moving_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moving_type', to='information.moving_type')),
                ('price_satisfaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_satisfaction', to='information.satisfaction')),
                ('professional_satisfaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professional_satisfaction', to='information.satisfaction')),
            ],
            options={
                'db_table': 'feedback_history',
            },
        ),
        migrations.AddField(
            model_name='company_car',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='information.moving_company_information'),
        ),
        migrations.AddField(
            model_name='application_of_moving',
            name='customer_information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.customerinfomation'),
        ),
    ]
