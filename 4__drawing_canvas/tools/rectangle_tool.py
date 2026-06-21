from typing import Optional, cast

from PySide6.QtCore import QPointF, QRectF
from PySide6.QtWidgets import (  
    QGraphicsSceneMouseEvent,
    QGraphicsScene,
    )
from tools.tool_protocol import Tool
from commands.add_item_command import AddItemCommand
from protocols.scene_protocol import SceneProtocol
from items.rectangle_item import RectangleItem

class RectangleTool(Tool):
    def __init__(self) -> None:
        self.start_pos: Optional[QPointF] = None
        self.item: Optional[RectangleItem] = None

    def mouse_press(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        self.start_pos: Optional[QPointF] = event.scenePos()

        self.item:Optional[RectangleItem] = RectangleItem()
        self.item.setFlag(
            RectangleItem.GraphicsItemFlag.ItemIsMovable,
            True,
        )

        self.item.setFlag(
            RectangleItem.GraphicsItemFlag.ItemIsSelectable,
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

        rect: QRectF = QRectF(
            self.start_pos,
            event.scenePos(),
        ).normalized()

        self.item.setRect(rect)

    def mouse_release(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        if not self.item:
            return
        
        command = AddItemCommand(self.item, scene)
        canvas_scene: SceneProtocol = cast(SceneProtocol, scene)
        canvas_scene.command_manager.undo_stack.append(command)

        self.item: Optional[RectangleItem] = None