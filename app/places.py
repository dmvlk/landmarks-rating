def add_place(
    places: list[dict],
    name: str,
    address: str,
    description: str,
) -> dict | None:
    if len(name.strip()) < 3:
        print("Ошибка: название места слишком короткое")
        return None
    if len(address.strip()) < 3:
        print("Ошибка: адрес слишком короткий")
        return None
    if len(description.strip()) < 3:
        print("Ошибка: описание слишком короткое")
        return None

    new_id = _next_id(places)
    place = {
        "id": new_id,
        "name": name.strip(),
        "address": address.strip(),
        "description": description.strip(),
    }
    places.append(place)
    return place


def find_place_by_id(places: list[dict], place_id: int) -> dict | None:
    for place in places:
        if place["id"] == place_id:
            return place
    return None


def find_places_by_name(places: list[dict], query: str) -> list[dict]:
    query_lower = query.strip().lower()
    result = []
    for place in places:
        if query_lower in place["name"].lower():
            result.append(place)
    return result


def delete_place(
    places: list[dict],
    reviews: list[dict],
    place_id: int,
) -> bool:
    place = find_place_by_id(places, place_id)
    if place is None:
        print("Ошибка: место не найдено")
        return False

    # удаляем отзывы, привязанные к этому месту
    reviews[:] = [r for r in reviews if r["place_id"] != place_id]
    places.remove(place)
    return True


def show_places(places: list[dict]) -> None:
    if not places:
        print("Список мест пуст")
        return
    for place in places:
        print(f"[{place['id']}] {place['name']} — {place['address']}")
        print(f"    {place['description']}")


def _next_id(places: list[dict]) -> int:
    if not places:
        return 1
    max_id = 0
    for place in places:
        if place["id"] > max_id:
            max_id = place["id"]
    return max_id + 1
