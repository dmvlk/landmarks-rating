"""Перенос данных из старой SQLite (ПР7) в базу Django ORM."""
import os
import sys
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from places.models import Place
from reviews.models import Review
from django.contrib.auth.models import User

SOURCE_DB = BASE_DIR / "data" / "landmarks.sqlite"


def main():
    if not SOURCE_DB.exists():
        print(f"Файл {SOURCE_DB} не найден!")
        return

    with sqlite3.connect(SOURCE_DB) as conn:
        conn.row_factory = sqlite3.Row

        places_data = conn.execute("SELECT * FROM places").fetchall()
        for row in places_data:
            Place.objects.update_or_create(
                id=row["id"],
                defaults={
                    "name": row["name"],
                    "address": row["address"],
                    "description": row["description"],
                }
            )

        users_data = conn.execute("SELECT * FROM users").fetchall()
        for row in users_data:
            User.objects.update_or_create(
                id=row["id"],
                defaults={
                    "username": row["name"].replace(" ", "_").lower(),
                    "email": row["email"],
                }
            )

        reviews_data = conn.execute("SELECT * FROM reviews").fetchall()
        for row in reviews_data:
            Review.objects.update_or_create(
                id=row["id"],
                defaults={
                    "place_id": row["place_id"],
                    "user_id": row["user_id"],
                    "rating": row["rating"],
                    "comment": row["comment"],
                }
            )

    print("Данные успешно перенесены в базу Django ORM")


if __name__ == "__main__":
    main()
