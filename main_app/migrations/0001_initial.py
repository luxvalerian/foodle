# Generated by Django 3.0.4 on 2020-04-17 00:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True,
                                                max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                                               max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True,
                                            max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_customer', models.BooleanField(default=False)),
                ('is_volunteer', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('unit_price', models.FloatField(verbose_name='Price')),
                ('unit_measurement', models.CharField(choices=[('E', 'Each'), ('L', 'LB'), ('O', 'OZ'), ('F', 'FL OZ'), ('U', 'Unit'), (
                    'G', 'Gram'), ('K', 'KG'), ('M', 'GL'), ('D', 'Dozen')], default='E', max_length=1, verbose_name='Measurement Units')),
                ('image', models.CharField(max_length=1000, verbose_name='Image URL')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_customer', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('timeslot', models.CharField(choices=[('A', '9AM–10AM'), ('B', '10AM–11AM'), ('C', '11AM–12PM'), ('D', '12PM–1PM'), ('E', '1PM–2PM'), ('F', '2PM–3PM'), ('G', '3PM–4PM'), (
                    'H', '4PM–5PM'), ('I', '5PM–6PM'), ('J', '6PM–7PM'), ('K', '7PM–8PM'), ('L', '8PM–9PM'), ('M', '9PM–10PM')], default='A', max_length=1, verbose_name='Timeslot')),
                << << << < HEAD
                ('customer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main_app.Customer')),
                ('volunteer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main_app.Volunteer')),
                == == == =
                ('volunteer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main_app.Customer')),
                >>>>>> > 85cb0eff5a8913c7f78722b04af718c048468cd5
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='main_app.Item')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main_app.Customer')),
            ],
        ),
    ]
