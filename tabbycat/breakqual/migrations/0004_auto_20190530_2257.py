# Generated by Django 2.2.1 on 2019-05-30 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakqual', '0003_breakcategory_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakcategory',
            name='rule',
            field=models.CharField(choices=[('standard', 'Standard'), ('aida-1996', 'AIDA 1996'), ('aida-2016-easters', 'AIDA 2016 (Easters)'), ('aida-2016-australs', 'AIDA 2016 (Australs)'), ('aida-2019-australs-open', 'AIDA 2019 (Australs, Dynamic Cap)'), ('wadl-div-first', 'WADL division winners first'), ('wadl-div-guaranteed', 'WADL division winners guaranteed')], default='standard', help_text='Rule for how the break is calculated (most tournaments should use "Standard")', max_length=25, verbose_name='rule'),
        ),
    ]
