# Generated by Django 1.10.4 on 2019-02-08 02:44


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctirs', '0005_auto_20190110_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='GVAuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_l1_view', models.BooleanField(default=True)),
                ('is_l2_view', models.BooleanField(default=True)),
                ('is_sharing_view', models.BooleanField(default=False)),
                ('css_thema', models.CharField(default=b'default', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='stipuser',
            name='gv_auth_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ctirs.GVAuthUser'),
        ),
    ]
