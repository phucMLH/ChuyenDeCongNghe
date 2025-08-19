from django.core.management.base import BaseCommand
from polls.models import Author, Book
from random import randint, choice

class Command(BaseCommand):
    help = "Generate sample Authors & Books"

    def handle(self, *args, **options):
        authors = []
        for name in ["Jane Austen", "George Orwell", "Tolkien", "Murakami", "Rowling"]:
            a, _ = Author.objects.get_or_create(name=name)
            authors.append(a)

        titles = [
            "Pride and Prejudice", "1984", "Animal Farm",
            "The Hobbit", "Kafka on the Shore", "Norwegian Wood",
            "Harry Potter and the Goblet of Fire"
        ]

        for t in titles:
            Book.objects.get_or_create(
                title=t,
                defaults={
                    "published_year": randint(1850, 2020),
                    "author": choice(authors),
                },
            )

        self.stdout.write(self.style.SUCCESS("Seeded authors & books."))
