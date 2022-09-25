from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('m_name', models.CharField(max_length=50, null=True)),
                ('l_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Prefer not to respond', 'Prefer not to respond'), ('Male', 'Male'), ('Female', 'Female')], max_length=21)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Selected', 'Selected'), ('Rejected', 'Rejected')], max_length=8)),
                ('resume', models.FileField(blank=True, upload_to='resume')),
            ],
        ),
    ]
