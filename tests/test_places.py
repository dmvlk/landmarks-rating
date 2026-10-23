from app.places import add_place, find_places_by_name, delete_place


def test_add_place():
    places = []
    add_place(places, "Парк Горького", "Москва", "Центральный парк")
    assert len(places) == 1
    assert places[0]["name"] == "Парк Горького"


def test_find_places_by_name():
    places = []
    add_place(places, "Парк Горького", "Москва", "Центральный парк")
    add_place(places, "Эрмитаж", "СПб", "Музей")
    found = find_places_by_name(places, "парк")
    assert len(found) == 1
    assert found[0]["name"] == "Парк Горького"


def test_delete_place_with_reviews():
    places = []
    reviews = []
    place = add_place(places, "Парк Горького", "Москва", "Центральный парк")
    reviews.append({
        "id": 1,
        "place_id": place["id"],
        "rating": 5,
        "comment": "Класс"})

    delete_place(places, reviews, place["id"])
    assert len(places) == 0
    assert len(reviews) == 0
