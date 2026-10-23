from app.models import User


def add_user(users: list[User], name: str, email: str) -> User:
    new_id = _next_id(users)
    user = User(new_id, name, email)
    users.append(user)
    return user


def find_user_by_id(users: list[User], user_id: int) -> User | None:
    for user in users:
        if user.id == user_id:
            return user
    return None


def show_users(users: list[User]) -> None:
    if not users:
        print("Список пользователей пуст")
        return
    for user in users:
        print(f"[{user.id}] {user.name} ({user.email})")


def _next_id(users: list[User]) -> int:
    if not users:
        return 1
    return max(user.id for user in users) + 1
