from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_data = [
            {"title": "Cozy Apartment in Paris", "description": "A beautiful apartment in the heart of Paris.", "price_per_night": 120.00, "location": "Paris"},
            {"title": "Beach House in Bali", "description": "Relax and enjoy the ocean view.", "price_per_night": 200.00, "location": "Bali"},
            {"title": "Mountain Cabin in Colorado", "description": "Perfect for a winter getaway.", "price_per_night": 150.00, "location": "Colorado"},
        ]

        for data in sample_data:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "price_per_night": data["price_per_night"],
                    "location": data["location"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
