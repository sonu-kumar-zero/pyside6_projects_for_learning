from PySide6.QtWidgets import QGraphicsEllipseItem
from PySide6.QtCore import  QRectF

from items.graphics_item_type import GraphicsItemType
from items.base_item import BaseItem
from items.movable_item_mixin import MovableItemMixin

from models.shape import ShapeData

class EllipseItem(
    MovableItemMixin,
    QGraphicsEllipseItem,
    BaseItem):
    ITEM_TYPE = GraphicsItemType.ELLIPSE
    def __init__(self, rect: QRectF | None = None):
        QGraphicsEllipseItem.__init__(self, rect or QRectF())
        MovableItemMixin.__init__(self)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsFocusable, True)
        
    def to_dict(self) -> dict[str, float | str]:
        rect = self.rect()
        return ShapeData(
            type=self.ITEM_TYPE.value,
            x=rect.x(),
            y=rect.y(),
            width=rect.width(),
            height=rect.height(),
            pos_x=self.pos().x(),
            pos_y=self.pos().y()
        ).to_dict()

    @classmethod
    def from_dict(cls, data: ShapeData) -> 'EllipseItem':
        rect = QRectF(
                data.x,
                data.y,
                data.width,
                data.height
            )
        item = cls(rect)
        item.setPos(data.pos_x, data.pos_y)
        return item