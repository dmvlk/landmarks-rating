from app.places import add_place
from app.reviews import add_review, get_average_rating


def test_add_review():
    places = []
    reviews = []
    place = add_place(places, "Парк", "Москва", "Описание")

    add_review(reviews, places, place["id"], 5, "Отличное место")
    assert len(reviews) == 1
    assert reviews[0]["rating"] == 5


def test_average_rating():
    places = []
    reviews = []
    place = add_place(places, "Парк", "Москва", "Описание")

    add_review(reviews, places, place["id"], 4, "Хорошо")
    add_review(reviews, places, place["id"], 5, "Отлично")

    avg = get_average_rating(reviews, place["id"])
    assert avg == 4.5
