from app.storage import load_places, load_reviews, load_users
from app.places import find_place_by_id
from django.shortcuts import render


def places(request):
    places_list = load_places("data/places.json")
    context = {"places": places_list}
    return render(request, "places/place_list.html", context)


def place_detail(request, place_id):
    places_list = load_places("data/places.json")
    users_list = load_users("data/users.json")
    reviews_list = load_reviews("data/reviews.json", places_list, users_list)

    place = find_place_by_id(places_list, place_id)

    if place is None:
        return render(
            request,
            "places/place_detail.html",
            {"place": None},
            status=404
        )

    place_reviews = [r for r in reviews_list if r.place.id == place_id]
    if place_reviews:
        avg_rating = sum(r.rating for r in place_reviews) / len(place_reviews)
        rating_text = f"{avg_rating:.1f} / 5 (отзывов: {len(place_reviews)})"
        rating_color = "text-warning" if avg_rating >= 4 else "text-secondary"
    else:
        rating_text = "Нет отзывов"
        rating_color = "text-muted"

    context = {
        "place": place,
        "rating_text": rating_text,
        "rating_color": rating_color,
    }

    return render(request, "places/place_detail.html", context)
