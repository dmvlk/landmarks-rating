from app.places import (
    add_place,
    delete_place,
    find_places_by_name,
    find_place_by_id,
    show_places,
)

from app.reviews import (
    add_review,
    delete_review,
    get_average_rating,
    show_reviews,
)

from app.storage import load_places, load_reviews, save_places, save_reviews
from app.utils import input_int, input_str

PLACES_FILE = "data/places.json"
REVIEWS_FILE = "data/reviews.json"


def show_menu() -> None:
    print("\nСистема отзывов о городских местах")
    print("1. Показать все места")
    print("2. Найти место по названию")
    print("3. Добавить место")
    print("4. Удалить место")
    print("5. Добавить отзыв")
    print("6. Показать все отзывы")
    print("7. Средняя оценка места")
    print("8. Удалить отзыв")
    print("0. Выход")


def main() -> None:
    places = load_places(PLACES_FILE)
    reviews = load_reviews(REVIEWS_FILE)

    while True:
        show_menu()
        choice = input_int("Выберите действие: ")

        if choice == 0:
            save_places(PLACES_FILE, places)
            save_reviews(REVIEWS_FILE, reviews)
            print("Данные сохранены. До встречи!")
            break

        elif choice == 1:
            show_places(places)

        elif choice == 2:
            query = input_str("Введите часть названия: ")
            found = find_places_by_name(places, query)
            if found:
                show_places(found)
            else:
                print("Ничего не найдено")

        elif choice == 3:
            name = input_str("Название: ", min_length=3)
            address = input_str("Адрес: ", min_length=3)
            description = input_str("Описание: ", min_length=3)
            place = add_place(places, name, address, description)
            if place:
                print(f"Место добавлено с ID {place['id']}")

        elif choice == 4:
            place_id = input_int("Введите ID места: ")
            if delete_place(places, reviews, place_id):
                print("Место и его отзывы удалены")

        elif choice == 5:
            place_id = input_int("ID места: ")
            rating = input_int("Оценка (1-5): ")
            comment = input_str("Комментарий: ", min_length=3)
            review = add_review(reviews, places, place_id, rating, comment)
            if review:
                print(f"Отзыв добавлен с ID {review['id']}")

        elif choice == 6:
            show_reviews(reviews, places)

        elif choice == 7:
            place_id = input_int("ID места: ")
            place = find_place_by_id(places, place_id)
            if place:
                avg = get_average_rating(reviews, place_id)
                print(f"Средняя оценка '{place['name']}': {avg:.1f}")
            else:
                print("Место не найдено")

        elif choice == 8:
            review_id = input_int("Введите ID отзыва: ")
            if delete_review(reviews, review_id):
                print("Отзыв удалён")

        else:
            print("Некорректный пункт меню")


if __name__ == "__main__":
    main()
