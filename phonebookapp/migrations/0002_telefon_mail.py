# Generated by Django 2.2.5 on 2019-09-02 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phonebookapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefon_Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonebookapp.Email')),
            ],
        ),
    ]
