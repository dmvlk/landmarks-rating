import json
from db.database import get_connection

PLACES_FILE = "data/places.json"
USERS_FILE = "data/users.json"
REVIEWS_FILE = "data/reviews.json"


def load_json(filename: str) -> list:
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def import_places(conn):
    places = load_json(PLACES_FILE)
    conn.executemany(
        """
        INSERT INTO places (id, name, address, description)
        VALUES (?, ?, ?, ?)
        """,
        [
            (p["id"], p["name"], p["address"], p["description"])
            for p in places
        ],
    )


def import_users(conn):
    users = load_json(USERS_FILE)
    conn.executemany(
        """
        INSERT INTO users (id, name, email)
        VALUES (?, ?, ?)
        """,
        [(u["id"], u["name"], u["email"]) for u in users],
    )


def import_reviews(conn):
    reviews = load_json(REVIEWS_FILE)
    conn.executemany(
        """
        INSERT INTO reviews (id, place_id, user_id, rating, comment)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (
                r["id"],
                r["place_id"],
                r["user_id"],
                r["rating"],
                r["comment"],
            )
            for r in reviews
        ],
    )


def main():
    conn = get_connection()
    try:
        import_places(conn)
        import_users(conn)
        import_reviews(conn)
        conn.commit()
        print("Данные успешно перенесены в SQLite")
    except Exception as e:
        conn.rollback()
        print(f"Ошибка импорта: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
