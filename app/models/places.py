class Place:
    def __init__(self,
                 place_id: int,
                 name: str, address: str,
                 description: str) -> None:
        """Создать объект места."""
        self.id = place_id
        self.name = name
        self.address = address
        self.description = description

    def is_valid(self) -> bool:
        return (
            len(self.name.strip()) >= 3
            and len(self.address.strip()) >= 3
            and len(self.description.strip()) >= 3
        )

    def __str__(self) -> str:
        return f"[{self.id}] {self.name} — {self.address}"

    @classmethod
    def from_data(cls, data: dict) -> "Place":
        return cls(
            place_id=data["id"],
            name=data["name"],
            address=data["address"],
            description=data["description"],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "description": self.description,
        }
