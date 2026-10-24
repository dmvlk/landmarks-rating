from django.http import HttpResponse
from homepage.views import page
from app.storage import load_places, load_reviews, load_users
from app.places import find_place_by_id


def places(request):
    places_list = load_places("data/places.json")
    items = ""
    for place in places_list:
        items += f"""
        <div class="col-md-6 mb-4">
            <div class="card h-100 shadow-sm border-0">
                <div class="card-body">
                    <h5 class="card-title fw-bold">{place.name}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">
                        {place.address}
                    </h6>
                    <p class="card-text">{place.description}</p>
                    <a href="/places/{place.id}/"
                        class="btn btn-sm btn-custom mt-auto">
                        Подробнее
                    </a>
                </div>
            </div>
        </div>
        """
    if not items:
        items = """
        <div class="col-12">
            <div class="card shadow-sm border-0 p-4 text-muted">
                Пока нет добавленных мест.
            </div>
        </div>
        """

    content = f"""
    <h1 class="mb-4 fw-bold">Городские места</h1>
    <div class="row">{items}</div>
    """
    return HttpResponse(page("Места", content))


def place_detail(request, place_id):
    places_list = load_places("data/places.json")
    users_list = load_users("data/users.json")
    reviews_list = load_reviews("data/reviews.json", places_list, users_list)

    place = find_place_by_id(places_list, place_id)
    if place is None:
        content = """
        <div class="alert alert-danger shadow-sm">
            <h4>Место не найдено</h4>
            <a href="/places/"
                class="btn btn-outline-danger mt-2">
                К списку мест
            </a>
        </div>
        """
        return HttpResponse(page("Не найдено", content), status=404)

    place_reviews = [r for r in reviews_list if r.place.id == place_id]
    if place_reviews:
        avg_rating = sum(r.rating for r in place_reviews) / len(place_reviews)
        rating_text = f"{avg_rating:.1f} / 5 (отзывов: {len(place_reviews)})"
        rating_color = "text-warning" if avg_rating >= 4 else "text-secondary"
    else:
        rating_text = "Нет отзывов"
        rating_color = "text-muted"

    content = f"""
    <div class="card shadow-sm border-0 mb-4">
        <div class="card-body p-4">
            <h1 class="card-title fw-bold">{place.name}</h1>
            <h6 class="text-muted mb-3">📍 {place.address}</h6>
            <p class="lead">{place.description}</p>
            <hr>
            <p class="fs-5">
                <strong>Средняя оценка:</strong>
                <span class="{rating_color} fw-bold">{rating_text}</span>
            </p>
            <a href="/places/"
                class="btn btn-outline-custom mt-2">
                Назад к местам
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(place.name, content))
