from django.shortcuts import render
from app.storage import load_places, load_reviews, load_users


def reviews(request):
    places_list = load_places("data/places.json")
    users_list = load_users("data/users.json")
    reviews_list = load_reviews("data/reviews.json", places_list, users_list)

    context = {"reviews": reviews_list}
    return render(request, "reviews/review_list.html", context)
