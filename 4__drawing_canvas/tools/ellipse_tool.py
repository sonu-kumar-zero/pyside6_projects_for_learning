from typing import Optional, cast

from PySide6.QtCore import QPointF, QRectF
from PySide6.QtWidgets import ( 
    QGraphicsSceneMouseEvent, 
    QGraphicsScene,
    )

from tools.tool_protocol import Tool
from commands.add_item_command import AddItemCommand
from canvas.canvas_scene import CanvasScene

from items.ellipse_item import EllipseItem

class EllipseTool(Tool):
    def __init__(self) -> None:
        self.start_pos: Optional[QPointF] = None
        self.item: Optional[EllipseItem] = None

    def mouse_press(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        self.start_pos: Optional[QPointF] = event.scenePos()

        self.item: Optional[EllipseItem] = EllipseItem()

        self.item.setFlag(
            EllipseItem.GraphicsItemFlag.ItemIsMovable,
            True,
        )

        self.item.setFlag(
            EllipseItem.GraphicsItemFlag.ItemIsSelectable,
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
        if self.item is None:
            return
        command = AddItemCommand(self.item, scene)
        canvas_scene: CanvasScene = cast(CanvasScene, scene)
        canvas_scene.command_manager.undo_stack.append(command)
    
        self.item: Optional[EllipseItem] = None