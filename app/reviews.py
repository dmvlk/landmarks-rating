from app.places import find_place_by_id


def add_review(
    reviews: list[dict],
    places: list[dict],
    place_id: int,
    rating: int,
    comment: str,
) -> dict | None:
    if find_place_by_id(places, place_id) is None:
        print("Ошибка: место не найдено")
        return None
    if not isinstance(rating, int) or rating < 1 or rating > 5:
        print("Ошибка: оценка должна быть целым числом от 1 до 5")
        return None
    if len(comment.strip()) < 3:
        print("Ошибка: комментарий слишком короткий")
        return None

    new_id = _next_id(reviews)
    review = {
        "id": new_id,
        "place_id": place_id,
        "rating": rating,
        "comment": comment.strip(),
    }
    reviews.append(review)
    return review


def delete_review(reviews: list[dict], review_id: int) -> bool:
    for review in reviews:
        if review["id"] == review_id:
            reviews.remove(review)
            return True

    print("Ошибка: отзыв не найден")
    return False


def get_average_rating(reviews: list[dict], place_id: int) -> float:
    total = 0
    count = 0
    for review in reviews:
        if review["place_id"] == place_id:
            total += review["rating"]
            count += 1
    if count == 0:
        return 0.0
    return total / count


def show_reviews(reviews: list[dict], places: list[dict]) -> None:
    if not reviews:
        print("Список отзывов пуст")
        return
    for review in reviews:
        place = find_place_by_id(places, review["place_id"])
        place_name = place["name"] if place else "Неизвестное место"
        print(f"[{review['id']}] {place_name} — оценка {review['rating']}")
        print(f"    {review['comment']}")


def _next_id(reviews: list[dict]) -> int:
    if not reviews:
        return 1
    max_id = 0
    for review in reviews:
        if review["id"] > max_id:
            max_id = review["id"]
    return max_id + 1
