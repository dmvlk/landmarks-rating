from .places import Place
from .users import User


class Review:
    def __init__(
            self,
            review_id: int,
            place: Place, user: User,
            rating: int, comment: str) -> None:

        self.id = review_id
        self.place = place
        self.user = user
        self.rating = rating
        self.comment = comment

    def is_valid(self) -> bool:
        return 1 <= self.rating <= 5 and len(self.comment.strip()) >= 3

    def __str__(self) -> str:
        return (
            f"[{self.id}] {self.user.name} о '{self.place.name}': "
            f"{self.rating}/5 — {self.comment}"
        )

    @classmethod
    def from_data(cls, data: dict, place: Place, user: User) -> "Review":
        return cls(
            review_id=data["id"],
            place=place,
            user=user,
            rating=data["rating"],
            comment=data["comment"],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "place_id": self.place.id,
            "user_id": self.user.id,
            "rating": self.rating,
            "comment": self.comment,
        }
