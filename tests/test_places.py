from app.models import Place
from app.places import add_place, find_places_by_name


def test_place_creation():
    place = Place(1, "Парк", "Москва", "Красиво")
    assert place.id == 1
    assert place.name == "Парк"


def test_add_place():
    places = []
    place = add_place(places, "Парк Горького", "Москва", "Центральный парк")
    assert len(places) == 1
    assert place.name == "Парк Горького"


def test_find_places_by_name():
    places = []
    add_place(places, "Парк Горького", "Москва", "Центральный парк")
    found = find_places_by_name(places, "парк")
    assert len(found) == 1
