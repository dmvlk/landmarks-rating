def input_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: нужно ввести целое число")


def input_str(prompt: str, min_length: int = 1) -> str:
    while True:
        value = input(prompt).strip()
        if len(value) < min_length:
            print(f"Ошибка: длина не меньше {min_length} символов")
            continue
        return value
