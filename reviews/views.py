from django.shortcuts import render
from reviews.models import Review


def reviews(request):
    reviews_list = Review.objects.select_related(
        "place", "user"
    ).order_by("-id")

    context = {"reviews": reviews_list}
    return render(request, "reviews/review_list.html", context)
