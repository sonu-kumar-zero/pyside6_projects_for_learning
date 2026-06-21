from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QRectF

from items.graphics_item_type import GraphicsItemType
from items.base_item import BaseItem

class RectangleItem(QGraphicsRectItem, BaseItem):
    ITEM_TYPE = GraphicsItemType.RECTANGLE
    
    def __init__(self, rect:QRectF | None = None):
        super().__init__(rect or QRectF())
        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsFocusable, True)
        
    def to_dict(self) -> dict[str, float | str]:
        rect = self.rect()
        return {
            "type": "rectangle",
            "x": rect.x(),
            "y": rect.y(),
            "width": rect.width(),
            "height": rect.height(),
            "pos_x": self.pos().x(),
            "pos_y": self.pos().y(),
        }
    
    @classmethod
    def from_dict(cls, data: dict[str, float | str]) -> 'RectangleItem':
        item = cls(
            QRectF(
                float(data["x"]),
                float(data["y"]),
                float(data["width"]),
                float(data["height"])
            )
        )
        item.setPos(float(data["pos_x"]), float(data["pos_y"]))
        return item