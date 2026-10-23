from app.models import Place, User
from app.reviews import add_review, get_average_rating


def test_add_review():
    places = [Place(1, "Парк", "Москва", "Красиво")]
    user = User(1, "Тест", "test@gmail.com")
    reviews = []

    review = add_review(reviews, places, 1, user, 5, "Отлично")
    assert len(reviews) == 1
    assert review.rating == 5


def test_average_rating():
    places = [Place(1, "Парк", "Москва", "Красиво")]
    user = User(1, "Тест", "test@gmail.com")
    reviews = []

    add_review(reviews, places, 1, user, 4, "Хорошо")
    add_review(reviews, places, 1, user, 5, "Отлично")

    avg = get_average_rating(reviews, 1)
    assert avg == 4.5
