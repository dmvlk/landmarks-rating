import json


def load_places(filename: str) -> list[dict]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} поврежден, данные не загружены")
        return []


def save_places(filename: str, places: list[dict]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(places, f, ensure_ascii=False, indent=2)


def load_reviews(filename: str) -> list[dict]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} повреждён, данные не загружены")
        return []


def save_reviews(filename: str, reviews: list[dict]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
