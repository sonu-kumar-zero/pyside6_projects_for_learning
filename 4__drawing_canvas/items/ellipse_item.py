from PySide6.QtWidgets import QGraphicsEllipseItem
from PySide6.QtCore import  QRectF

from items.graphics_item_type import GraphicsItemType
from items.base_item import BaseItem

class EllipseItem(QGraphicsEllipseItem, BaseItem):
    ITEM_TYPE = GraphicsItemType.ELLIPSE
    def __init__(self, rect: QRectF | None = None):
        super().__init__(rect or QRectF())
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsFocusable, True)
        
    def to_dict(self) -> dict[str, float | str]:
        rect = self.rect()
        return {
            "type": "ellipse",
            "x": rect.x(),
            "y": rect.y(),
            "width": rect.width(),
            "height": rect.height(),
            "pos_x": self.pos().x(),
            "pos_y": self.pos().y(),
        }
    
    @classmethod
    def from_dict(cls, data: dict[str, float | str]) -> 'EllipseItem':
        rect = QRectF(
            float(data["x"]), 
            float(data["y"]), 
            float(data["width"]), 
            float(data["height"])
            )
        item = cls(rect)
        item.setPos(float(data["pos_x"]), float(data["pos_y"]))
        return item