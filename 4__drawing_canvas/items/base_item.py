from items.graphics_item_type import GraphicsItemType
from models.shape import ShapeData

from PySide6.QtCore import QPointF

class BaseItem:
    ITEM_TYPE: GraphicsItemType
    
    def __init__(self):
        self._old_pos = QPointF()
    
    def item_type(self) -> GraphicsItemType:
        return self.ITEM_TYPE

    def to_dict(self) -> dict[str, float | str]:
        raise NotImplementedError("Subclasses must implement to_dict method")
    
    @classmethod
    def from_dict(cls, data: ShapeData) -> 'BaseItem':
        raise NotImplementedError("Subclasses must implement from_dict method")