from app.models import Place


def add_place(places: list[Place],
              name: str,
              address: str,
              description: str) -> Place | None:

    new_id = _next_id(places)
    place = Place(new_id, name, address, description)

    if not place.is_valid():
        print(
            "Ошибка: данные места некорректны "
            "(поля должны быть не короче 3 символов)"
        )
        return None

    places.append(place)
    return place


def find_place_by_id(places: list[Place], place_id: int) -> Place | None:
    for place in places:
        if place.id == place_id:
            return place
    return None


def find_places_by_name(places: list[Place], query: str) -> list[Place]:
    query_lower = query.strip().lower()
    return [place for place in places if query_lower in place.name.lower()]


def delete_place(places: list[Place], reviews: list, place_id: int) -> bool:
    place = find_place_by_id(places, place_id)
    if place is None:
        print("Ошибка: место не найдено")
        return False

    # удаляем отзывы, привязанные к этому месту
    reviews[:] = [r for r in reviews if r.place.id != place_id]
    places.remove(place)
    return True


def show_places(places: list[Place]) -> None:
    if not places:
        print("Список мест пуст")
        return
    for place in places:
        print(place)
        print(f"    {place.description}")


def _next_id(places: list[Place]) -> int:
    if not places:
        return 1

    return max(place.id for place in places) + 1
