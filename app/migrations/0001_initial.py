# Generated by Django 4.2.15 on 2024-08-08 01:58

import cloudinary.models
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import pyotp


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='username')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=255, null=True, verbose_name='gender')),
                ('avatar', cloudinary.models.CloudinaryField(default='image/upload/v1723017084/wlwartuoohu21c2wzu8k.png', max_length=255, verbose_name='avatar')),
                ('default_address', models.TextField(verbose_name='default address')),
                ('default_phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits and start with 0.', regex='^0\\d{9}$')], verbose_name='default phone number')),
                ('otp_secret', models.CharField(blank=True, default=pyotp.random_base32, max_length=32, null=True, verbose_name='OTP secret')),
                ('otp_created_at', models.DateTimeField(blank=True, null=True, verbose_name='OTP created at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='address')),
                ('phone_number', models.CharField(max_length=10, verbose_name='phone number')),
                ('status', models.CharField(choices=[('Wait_for_pay', 'Wait for pay'), ('Wait_for_preparing', 'Wait for preparing'), ('Wait_for_delivery', 'Wait for delivery'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=255, verbose_name='status')),
                ('note_content', models.TextField(blank=True, null=True, verbose_name='note content')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total')),
                ('payment_method', models.CharField(choices=[('CASH', 'Cash'), ('VISA', 'Visa'), ('BANK', 'Bank')], max_length=255, verbose_name='payment method')),
                ('expired_at', models.DateTimeField(blank=True, null=True, verbose_name='expired at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'bill',
                'verbose_name_plural': 'bills',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the category.', max_length=255, unique=True, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='price')),
                ('description', models.TextField(verbose_name='description')),
                ('average_rating', models.FloatField(verbose_name='average rating')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(verbose_name='discount')),
                ('started_at', models.DateTimeField(verbose_name='started at')),
                ('ended_at', models.DateTimeField(verbose_name='ended at')),
                ('min_amount', models.DecimalField(blank=True, decimal_places=0, default=0, help_text='Minimum amount required to apply this voucher.', max_digits=10, verbose_name='minimum amount')),
                ('is_global', models.BooleanField(default=False, verbose_name='is global')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('category', models.ManyToManyField(blank=True, help_text='Categories this condition applies to.', to='app.category', verbose_name='categories')),
                ('user', models.ForeignKey(blank=True, help_text='User to whom this voucher is assigned.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'voucher',
                'verbose_name_plural': 'vouchers',
            },
        ),
        migrations.CreateModel(
            name='VoucherHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.voucher', verbose_name='voucher')),
            ],
            options={
                'verbose_name': 'voucher history',
                'verbose_name_plural': 'voucher histories',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='image/upload/v1723015712/byvk6iveofgnb1xf7dsz.jpg', max_length=255, verbose_name='image')),
                ('size', models.CharField(blank=True, choices=[('S', 'S'), ('XS', 'XS'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=255, null=True, verbose_name='size')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='color')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='price')),
                ('remain_quantity', models.IntegerField(verbose_name='remaining quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product detail',
                'verbose_name_plural': 'product details',
                'ordering': ['product'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('star', models.IntegerField(verbose_name='star')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cart', verbose_name='cart')),
                ('product_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productdetail', verbose_name='product detail')),
            ],
            options={
                'verbose_name': 'cart detail',
                'verbose_name_plural': 'cart details',
            },
        ),
        migrations.CreateModel(
            name='BillDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bill', verbose_name='bill')),
                ('product_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productdetail', verbose_name='product detail')),
            ],
            options={
                'verbose_name': 'bill detail',
                'verbose_name_plural': 'bill details',
                'ordering': ['bill'],
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.voucher', verbose_name='voucher'),
        ),
    ]