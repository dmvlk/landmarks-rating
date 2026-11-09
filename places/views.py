from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count
from places.models import Place


def places(request):
    places_list = Place.objects.order_by("name")
    places_list = places_list.annotate(
        avg_rating=Avg("reviews__rating"),
        reviews_count=Count("reviews")
    )

    context = {"places": places_list}
    return render(request, "places/place_list.html", context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    rating_info = place.reviews.aggregate(
        avg_rating=Avg("rating"),
        count=Count("id")
    )

    if rating_info["count"] > 0:
        rating_text = (
            f"{rating_info['avg_rating']:.1f} / 5 "
            f"(отзывов: {rating_info['count']})"
        )
        rating_color = (
            "text-warning" if rating_info["avg_rating"] >= 4
            else "text-secondary"
        )
    else:
        rating_text = "Нет отзывов"
        rating_color = "text-muted"

    context = {
        "place": place,
        "rating_text": rating_text,
        "rating_color": rating_color,
    }

    return render(request, "places/place_detail.html", context)
