from app.places import find_place_by_id
from app.models import Place, Review, User


def add_review(
    reviews: list[Review],
    places: list[Place],
    place_id: int,
    user: User,
    rating: int,
    comment: str,
) -> Review | None:
    """Создать отзыв."""
    place = find_place_by_id(places, place_id)
    if place is None:
        print("Ошибка: место не найдено")
        return None

    new_id = _next_id(reviews)
    review = Review(new_id, place, user, rating, comment)

    if not review.is_valid():
        print(
            "Ошибка: некорректная оценка (1-5) "
            "или слишком короткий комментарий"
        )
        return None

    reviews.append(review)
    return review


def delete_review(reviews: list[Review], review_id: int) -> bool:
    for review in reviews:
        if review.id == review_id:
            reviews.remove(review)
            return True

    print("Ошибка: отзыв не найден")
    return False


def get_average_rating(reviews: list[Review], place_id: int) -> float:
    target_reviews = [r for r in reviews if r.place.id == place_id]
    if not target_reviews:
        return 0.0
    total = sum(r.rating for r in target_reviews)
    return total / len(target_reviews)


def show_reviews(reviews: list[Review]) -> None:
    if not reviews:
        print("Список отзывов пуст")
        return
    for review in reviews:
        print(review)


def _next_id(reviews: list[Review]) -> int:
    if not reviews:
        return 1
    return max(review.id for review in reviews) + 1
