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