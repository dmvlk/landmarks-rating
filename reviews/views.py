from django.shortcuts import render
from db.database import get_connection


def reviews(request):
    conn = get_connection()
    rows = conn.execute("""
        SELECT
            reviews.id,
            reviews.rating,
            reviews.comment,
            places.name AS place_name,
            users.name AS user_name
        FROM reviews
        JOIN places ON reviews.place_id = places.id
        JOIN users ON reviews.user_id = users.id
        ORDER BY reviews.id DESC
    """).fetchall()
    conn.close()

    reviews_data = [dict(row) for row in rows]

    context = {"reviews": reviews_data}
    return render(request, "reviews/review_list.html", context)
