from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from modules.product.models import Product

class Command(BaseCommand):
    help = 'Loads sample product data into the database'

    def handle(self, *args, **kwargs):
        # Create a sample user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='sample_user',
            defaults={
                'email': 'sample@example.com',
                'is_staff': True
            }
        )
        if created:
            user.set_password('samplepass123')
            user.save()
            self.stdout.write(self.style.SUCCESS('Created sample user'))

        # Sample product data
        products = [
            {
                'name': 'iPhone 15 Pro',
                'barcode': 'IP15P-001',
                'price': 999.99,
                'stock': 50,
                'user': user
            },
            {
                'name': 'MacBook Pro M3',
                'barcode': 'MBP-M3-001',
                'price': 1999.99,
                'stock': 25,
                'user': user
            },
            {
                'name': 'AirPods Pro',
                'barcode': 'APP-001',
                'price': 249.99,
                'stock': 100,
                'user': user
            },
            {
                'name': 'iPad Air',
                'barcode': 'IPA-001',
                'price': 599.99,
                'stock': 75,
                'user': user
            },
            {
                'name': 'Apple Watch Series 9',
                'barcode': 'AWS9-001',
                'price': 399.99,
                'stock': 30,
                'user': user
            }
        ]

        # Create products
        for product_data in products:
            product, created = Product.objects.get_or_create(
                barcode=product_data['barcode'],
                defaults=product_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample products')) 