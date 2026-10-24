from django.http import HttpResponse
from homepage.views import page
from app.storage import load_places, load_reviews, load_users


def reviews(request):
    places_list = load_places("data/places.json")
    users_list = load_users("data/users.json")
    reviews_list = load_reviews("data/reviews.json", places_list, users_list)

    items = ""
    for review in reviews_list:
        stars = "★" * review.rating + "☆" * (5 - review.rating)
        items += f"""
        <li class="list-group-item p-4">
            <div
                class="d-flex justify-content-between align-items-center mb-2">
                <h5 class="mb-0 fw-bold">{review.place.name}</h5>
                <span class="fs-5" style="color: #c9ada7;">{stars}</span>
            </div>
            <p class="mb-2">{review.comment}</p>
            <small class="text-muted">Автор: {review.user.name}</small>
        </li>
        """

    if not items:
        items = (
            '<li class="list-group-item p-4 text-muted">'
            'Пока нет отзывов.</li>'
        )

    content = f"""
    <h1 class="mb-4 fw-bold">Последние отзывы</h1>
    <ul class="list-group shadow-sm border-0">{items}</ul>
    """
    return HttpResponse(page("Отзывы", content))
