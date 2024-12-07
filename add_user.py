import os
import django

# Đặt biến môi trường cho cài đặt Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'work_management.settings')
django.setup()

from django.contrib.auth.models import User

# Tạo user mới
user = User.objects.create_user(username='admin', password='admin', email='ngletuan94@gmail.com')

# Lưu user
user.save()
