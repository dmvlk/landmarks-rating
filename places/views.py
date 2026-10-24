from django.shortcuts import render
from db.database import get_connection


def places(request):
    conn = get_connection()
    rows = conn.execute("""
        SELECT id, name, address, description 
        FROM places 
        ORDER BY name
    """).fetchall()
    conn.close()

    places_data = [dict(row) for row in rows]

    context = {"places": places_data}
    return render(request, "places/place_list.html", context)


def place_detail(request, place_id):
    conn = get_connection()

    row = conn.execute(
        "SELECT * FROM places WHERE id = ?", [place_id]
    ).fetchone()

    if row is None:
        conn.close()
        return render(
            request, "places/place_detail.html", {"place": None}, status=404
        )

    place = dict(row)

    rating_row = conn.execute("""
        SELECT AVG(rating) as avg_rating, COUNT(*) as count
        FROM reviews
        WHERE place_id = ?
    """, [place_id]).fetchone()

    rating_info = dict(rating_row)

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

    conn.close()

    context = {
        "place": place,
        "rating_text": rating_text,
        "rating_color": rating_color,
    }

    return render(request, "places/place_detail.html", context)
