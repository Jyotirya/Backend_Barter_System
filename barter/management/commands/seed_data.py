from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from barter.models import Item, BarterLog, ItemImage
from user.models import CustomUser

class Command(BaseCommand):
    help = 'Seeds the database with 20 sample items and barter logs'

    def handle(self, *args, **options):
        # Get or create sample users (sellers)
        seller1, _ = CustomUser.objects.get_or_create(
            email='seller1@example.com',
            defaults={
                'first_name': 'Marcus',
                'last_name': 'Lee',
                'password': 'temppass123'
            }
        )
        
        seller2, _ = CustomUser.objects.get_or_create(
            email='seller2@example.com',
            defaults={
                'first_name': 'Sarah',
                'last_name': 'Wilson',
                'password': 'temppass123'
            }
        )

        seller3, _ = CustomUser.objects.get_or_create(
            email='seller3@example.com',
            defaults={
                'first_name': 'John',
                'last_name': 'Doe',
                'password': 'temppass123'
            }
        )

        # 20 sample items from data.js
        items_data = [
            {'name': 'Vintage Camera', 'description': 'Retro 35mm film professional camera.', 'price': 120, 'condition': 'Used', 'tags': 'vintage, rare', 'seller': seller1, 'images': ['https://m.media-amazon.com/images/I/81Tib6mb8eL._AC_UY218_.jpg']},
            {'name': 'Mountain Bike', 'description': '21-speed mountain bike, lightly used.', 'price': 250, 'condition': 'Used', 'tags': 'sports, rare', 'seller': seller2, 'images': ['https://m.media-amazon.com/images/I/81Nm8hF59qL._AC_UY218_.jpg']},
            {'name': 'Acoustic Guitar', 'description': 'Full-size acoustic with case.', 'price': 150, 'condition': 'New', 'tags': 'other', 'seller': seller3, 'images': ['https://m.media-amazon.com/images/I/5133nEGq6dL._AC_UL640_QL65_.jpg']},
            {'name': 'Leather Backpack', 'description': 'Handcrafted water-resistant backpack.', 'price': 85, 'condition': 'Used', 'tags': 'other', 'seller': seller1, 'images': ['https://m.media-amazon.com/images/I/71hhHX9VsuL._AC_UL320_.jpg']},
            {'name': 'Coffee Maker', 'description': '12-cup programmable drip coffee maker.', 'price': 45, 'condition': 'Used', 'tags': 'kitchen', 'seller': seller2, 'images': ['https://m.media-amazon.com/images/I/51CG7fT4ShL._AC_UY218_.jpg']},
            {'name': 'Rope', 'description': 'Durable rope for every situation.', 'price': 15, 'condition': 'Used', 'tags': 'other', 'seller': seller3, 'images': ['https://imgs.search.brave.com/dzf_jvB20DGk1E3BnDIusZLJuSRcjwRwPDDyCbvMGJE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNjUx/NDI2OTM3L3Bob3Rv/L3NwYWluLXRvbGVk/by1yb3BlLXVzZWQt/YnktdGhlLXNwYW5p/c2gtaW5xdWlzaXRp/b24taW4tdGhlLTE2/dGgtY2VudHVyeS5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/SmRaRE1oWUotYV9x/NzllM3EzN0hGWFdC/M3MxZFR6TXJxVG43/aUdlaEdNRT0']},
            {'name': 'Smart Watch', 'description': 'Fitness smartwatch with heart-rate monitor.', 'price': 199, 'condition': 'Used', 'tags': 'watch', 'seller': seller1, 'images': ['https://m.media-amazon.com/images/I/61frMaBqWgL._AC_UY218_.jpg']},
            {'name': 'Ceramic Vase', 'description': 'Hand-painted decorative vase.', 'price': 30, 'condition': 'Used', 'tags': 'other', 'seller': seller2, 'images': ['https://m.media-amazon.com/images/I/61ZQkDvLwZL._AC_UL320_.jpg']},
            {'name': 'Board Game', 'description': 'Strategy board game for 2-6 players.', 'price': 40, 'condition': 'New', 'tags': 'toys', 'seller': seller3, 'images': ['https://m.media-amazon.com/images/I/61uX7ji6B5L._AC_UL320_.jpg']},
            {'name': 'Cocaine', 'description': 'High quality cocaine for recreational use.', 'price': 100, 'condition': 'New', 'tags': 'rare', 'seller': seller1, 'images': ['https://t4.ftcdn.net/jpg/14/16/02/13/240_F_1416021396_jYPJRRV5YAojTcPFHn6B5DYow89C6VAB.jpg']},
            {'name': 'Running Shoes', 'description': 'Lightweight running shoes, size 10.', 'price': 65, 'condition': 'Used', 'tags': 'sports', 'seller': seller2, 'images': ['https://m.media-amazon.com/images/I/61muHlVnHYL._AC_UL320_.jpg']},
            {'name': 'Desk Lamp', 'description': 'LED desk lamp with adjustable brightness.', 'price': 25, 'condition': 'Used', 'tags': 'electronics', 'seller': seller3, 'images': ['https://m.media-amazon.com/images/I/611AjN7Wq9L._AC_UL320_.jpg']},
            {'name': 'Headphones', 'description': 'Noise-cancelling over-ear headphones.', 'price': 180, 'condition': 'Used', 'tags': 'electronics', 'seller': seller1, 'images': ['https://m.media-amazon.com/images/I/71quB2GTUKL._AC_UY218_.jpg']},
            {'name': 'Yoga Mat', 'description': 'Eco-friendly non-slip mat, 6mm thickness.', 'price': 35, 'condition': 'Used', 'tags': 'sports', 'seller': seller2, 'images': ['https://m.media-amazon.com/images/I/71mInNZP1UL._AC_UL320_.jpg']},
            {'name': 'Bluetooth Speaker', 'description': 'Portable speaker with 10h battery.', 'price': 55, 'condition': 'New', 'tags': 'electronics', 'seller': seller3, 'images': ['https://m.media-amazon.com/images/I/71o6CU8MqVL._AC_UY218_.jpg']},
            {'name': 'Sketchbook Bundle', 'description': 'Set of 3 sketchbooks, 100gsm paper.', 'price': 20, 'condition': 'Used', 'tags': 'other', 'seller': seller1, 'images': ['https://m.media-amazon.com/images/I/715pEXpp-0L._AC_UL320_.jpg']},
            {'name': 'Electric Kettle', 'description': '1.7L stainless steel kettle for everyday use.', 'price': 38, 'condition': 'New', 'tags': 'kitchen', 'seller': seller2, 'images': ['https://m.media-amazon.com/images/I/61G2USexrDL._AC_UY218_.jpg']},
            {'name': 'Scented Candle Set', 'description': 'Pack of 4 soy wax candles.', 'price': 22, 'condition': 'Used', 'tags': 'other', 'seller': seller3, 'images': ['https://m.media-amazon.com/images/I/81mjkv25b5L._AC_UL320_.jpg']},
            {'name': 'Portable Charger', 'description': '10,000mAh power bank for charging on the go.', 'price': 30, 'condition': 'Used', 'tags': 'electronics', 'seller': seller1, 'images': ['https://m.media-amazon.com/images/I/51w9roMijiL._AC_UY218_.jpg']},
            {'name': 'Indoor Plant', 'description': 'Low-maintenance potted indoor plant.', 'price': 28, 'condition': 'Used', 'tags': 'other', 'seller': seller2, 'images': ['https://m.media-amazon.com/images/I/717UeE1dPyL._AC._SR360,460.jpg']},
        ]

        deadline = timezone.now() + timedelta(days=30)

        for item_data in items_data:
            images = item_data.pop('images')
            
            # Create or get item
            item, created = Item.objects.get_or_create(
                name=item_data['name'],
                seller=item_data['seller'],
                defaults={
                    'description': item_data['description'],
                    'price': item_data['price'],
                    'condition': item_data['condition'],
                    'tags': item_data['tags'],
                    'deadline': deadline
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created item: {item.name} ({item.itemId})')
                )
                
                # Create BarterLog entry
                BarterLog.objects.get_or_create(item=item)
                
                # Create item images
                for img_url in images:
                    ItemImage.objects.get_or_create(
                        item=item,
                        image_url=img_url
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Item already exists: {item.name}')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully seeded database with 20 sample items')
        )
