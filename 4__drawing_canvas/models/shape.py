from dataclasses import dataclass, asdict

@dataclass(slots=True)
class ShapeData:
    type: str
    x: float
    y: float
    width: float
    height: float
    pos_x: float
    pos_y: float
    
    def to_dict(self) -> dict[str, float | str]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, float | str]) -> "ShapeData":
        # Convert and cast values to the expected types to satisfy static type checkers
        return cls(
            type=str(data["type"]),
            x=float(data["x"]),
            y=float(data["y"]),
            width=float(data["width"]),
            height=float(data["height"]),
            pos_x=float(data["pos_x"]),
            pos_y=float(data["pos_y"]),
        )