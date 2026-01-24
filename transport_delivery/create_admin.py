import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_delivery.settings')
django.setup()

from django.contrib.auth.models import User

def ensure_admin(email, password, username):
    """Crée ou met à jour un compte admin."""
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print(f"  Admin mis à jour: {email}")
    elif User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        user.email = email
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print(f"  Admin mis à jour: {email}")
    else:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"  Admin créé: {email}")
    return user

# Comptes utilisables pour le frontend (email) et Django Admin (username)
print("Création des comptes administrateur...")
ensure_admin('admin@transport.com', 'admin123', 'admin')
ensure_admin('test@test.com', 'test123', 'testadmin')
print("Terminé. Compte principal: admin@transport.com / admin123")
