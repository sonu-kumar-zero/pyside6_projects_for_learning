from typing import Optional

from PySide6.QtCore import QPointF, QRectF
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsScene, QGraphicsSceneMouseEvent

class EllipseTool:
    def __init__(self) -> None:
        self.start_pos: Optional[QPointF] = None
        self.item: Optional[QGraphicsEllipseItem] = None

    def mouse_press(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        self.start_pos: Optional[QPointF] = event.scenePos()

        self.item: Optional[QGraphicsEllipseItem] = QGraphicsEllipseItem()

        self.item.setFlag(
            QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable,
            True,
        )

        self.item.setFlag(
            QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable,
            True,
        )

        scene.addItem(self.item)

    def mouse_move(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        if self.item is None or self.start_pos is None:
            return

        rect = QRectF(
            self.start_pos,
            event.scenePos(),
        ).normalized()

        self.item.setRect(rect)

    def mouse_release(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        self.item: Optional[QGraphicsEllipseItem] = None