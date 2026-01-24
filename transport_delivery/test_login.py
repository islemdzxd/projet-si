import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_delivery.settings')
django.setup()

from django.contrib.auth.models import User

print("=" * 60)
print("ALL USERS IN DATABASE:")
print("=" * 60)

for u in User.objects.all():
    print(f"ID: {u.id}")
    print(f"Email: [{u.email}]")
    print(f"Username: {u.username}")
    print(f"Superuser: {u.is_superuser}")
    print(f"Staff: {u.is_staff}")
    print("-" * 60)

print("\n" + "=" * 60)
print("TESTING LOGIN:")
print("=" * 60)

# Test test@test.com
try:
    user = User.objects.get(email='test@test.com')
    print(f"\nUser found: {user.username}")
    print(f"Password 'test123' check: {user.check_password('test123')}")
except User.DoesNotExist:
    print("\nUser test@test.com NOT FOUND!")

# Test admin@transport.com
try:
    user = User.objects.get(email='admin@transport.com')
    print(f"\nUser found: {user.username}")
    print(f"Password 'admin123' check: {user.check_password('admin123')}")
except User.DoesNotExist:
    print("\nUser admin@transport.com NOT FOUND!")

print("\n" + "=" * 60)
