# Generated by Django 2.1.1 on 2018-11-07 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=42)),
                ('last_changed', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('self_intro', models.CharField(blank=True, default="This person is lazy, (s)he didn't leave anything", max_length=420)),
                ('location', models.CharField(blank=True, default='NA', max_length=50)),
                ('job', models.CharField(blank=True, default='NA', max_length=50)),
                ('picture', models.ImageField(blank=True, default='photo_id/default.png', upload_to='profile_photos')),
                ('confirm', models.BooleanField(default=False)),
                ('token_reg', models.CharField(blank=True, default='', max_length=100)),
                ('token_reset', models.CharField(blank=True, default='', max_length=100)),
                ('friends', models.ManyToManyField(blank=True, to='glumblr.User_profile')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glumblr.User_profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glumblr.Message'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glumblr.User_profile'),
        ),
    ]
