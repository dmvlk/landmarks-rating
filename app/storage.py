import json
from app.models import Place, Review, User
from app.places import find_place_by_id
from app.users import find_user_by_id


def load_places(filename: str) -> list[Place]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Place.from_data(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_places(filename: str, places: list[Place]) -> None:
    data = [place.to_dict() for place in places]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_users(filename: str) -> list[User]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [User.from_data(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_users(filename: str, users: list[User]) -> None:
    data = [user.to_dict() for user in users]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_reviews(filename: str,
                 places: list[Place],
                 users: list[User]) -> list[Review]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            reviews = []
            for item in data:
                place = find_place_by_id(places, item["place_id"])
                user = find_user_by_id(users, item["user_id"])
                if place and user:
                    reviews.append(Review.from_data(item, place, user))
            return reviews
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_reviews(filename: str, reviews: list[Review]) -> None:
    data = [review.to_dict() for review in reviews]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
