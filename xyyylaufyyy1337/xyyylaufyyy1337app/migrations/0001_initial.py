from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Write',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=100)),
                ('bio', models.TextField(verbose_name='Bio')),
            ],
        ),
    ]