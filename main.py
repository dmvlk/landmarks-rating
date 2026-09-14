def create_place(name, address, description):
    if not isinstance(name, str) or len(name.strip()) < 3:
        return "Ошибка: название места слишком короткое"
    if not isinstance(address, str) or len(address.strip()) < 3:
        return "Ошибка: адрес слишком короткий"
    if not isinstance(description, str) or len(description.strip()) < 3:
        return "Ошибка: описание слишком короткое"
    return "Место корректно, можно создавать"


def delete_place(place_id, is_exists, is_owner):
    if not isinstance(place_id, int) or place_id <= 0:
        return "Ошибка: некорректный идентификатор места"
    if not is_exists:
        return "Ошибка: место не найдено"
    if not is_owner:
        return "Ошибка: удалять место может только его автор"
    return "Место можно удалить"


def create_review(rating, comment):
    if not isinstance(rating, int):
        return "Ошибка: оценка должна быть целым числом"
    if rating < 1 or rating > 5:
        return "Ошибка: оценка должна быть от 1 до 5"
    if not isinstance(comment, str) or len(comment.strip()) < 3:
        return "Ошибка: комментарий слишком короткий"
    return "Отзыв корректен, можно публиковать"


def delete_review(review_id, is_exists, is_author):
    if not isinstance(review_id, int) or review_id <= 0:
        return "Ошибка: некорректный идентификатор отзыва"
    if not is_exists:
        return "Ошибка: отзыв не найден"
    if not is_author:
        return "Ошибка: удалять отзыв может только его автор"
    return "Отзыв можно удалить"


def main():
    #создание места
    print(create_place("Парк Горького", "улица Пушкина, дом Колотушкина", "Центральный парк культуры и отдыха"))
    print(create_place("Аб", "Мск", "Ко"))

    #удаление места
    print(delete_place(1, True, True))
    print(delete_place(2, False, True))

    #создание отзыва
    print(create_review(5, "Хорошее место, рекомендую"))
    print(create_review(0, "Никогда не вернусь"))
    print(create_review("пять", "Хорошее место для прогулок"))

    #удаление отзыва
    print(delete_review(1, True, True))
    print(delete_review(5, True, False))


if __name__ == "__main__":
    main()