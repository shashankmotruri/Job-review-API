# Generated by Django 4.1.1 on 2022-09-24 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='m_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='l_name',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Decline to Answer', 'Decline to Answer')], max_length=21),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='resume',
            field=models.FileField(null=True, upload_to='resume'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Not Accepted', 'Not Accepted')], max_length=15),
        ),
    ]
