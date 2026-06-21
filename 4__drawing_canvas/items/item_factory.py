from PySide6.QtWidgets import QGraphicsItem
from typing import Type, cast

from items.graphics_item_type import GraphicsItemType
from items.rectangle_item import RectangleItem
from items.ellipse_item import EllipseItem
from items.base_item import BaseItem
from models.shape import ShapeData

ITEM_REGISTRY: dict[GraphicsItemType, Type[BaseItem]] = {
    GraphicsItemType.RECTANGLE: RectangleItem,
    GraphicsItemType.ELLIPSE: EllipseItem,
}

class ItemFactory:
    @staticmethod
    def create_item(data: ShapeData) -> QGraphicsItem:
        item_type = GraphicsItemType(data.type)

        item_class = ITEM_REGISTRY[item_type]

        return cast(QGraphicsItem, item_class.from_dict(data))
            