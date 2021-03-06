# Generated by Django 2.0.4 on 2018-04-09 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0008_auto_20180125_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statussurvey',
            name='bidcycle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='status_surveys', to='bidding.BidCycle'),
        ),
        migrations.AlterField(
            model_name='waiver',
            name='bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='waivers', to='bidding.Bid'),
        ),
        migrations.AlterField(
            model_name='waiver',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='waivers', to='position.Position'),
        ),
        migrations.AlterField(
            model_name='waiver',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reviewed_waivers', to='user_profile.UserProfile'),
        ),
        migrations.AlterField(
            model_name='waiver',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='waivers', to='user_profile.UserProfile'),
        ),
    ]
