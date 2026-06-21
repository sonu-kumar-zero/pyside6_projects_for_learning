from typing import cast

from PySide6.QtCore import QPointF
from PySide6.QtWidgets import (
    QGraphicsItem,
    QGraphicsSceneMouseEvent,
    
    )
from protocols.scene_protocol import SceneProtocol
from commands.move_item_command import MoveItemCommand


class MovableItemMixin:
    def __init__(self) -> None:
        self._old_pos = QPointF()
        
    def mousePressEvent(
        self, 
        event: QGraphicsSceneMouseEvent,
        ) -> None:
        self._old_pos = cast(QGraphicsItem, self).pos()
        QGraphicsItem.mousePressEvent(
            cast(QGraphicsItem, self),
            event,
        )

    def mouseReleaseEvent(
        self,
        event: QGraphicsSceneMouseEvent,
    ) -> None:
        new_pos = cast(QGraphicsItem, self).pos()
        
        if (
            self._old_pos - new_pos
        ).manhattanLength() > 0.1:
            scene = cast(QGraphicsItem, self).scene()

            if scene:
                canvas_scene = cast(
                    SceneProtocol, scene
                )
                command = MoveItemCommand(
                    cast(QGraphicsItem, self),
                    old_pos=QPointF(self._old_pos),
                    new_pos=QPointF(new_pos),
                )
                canvas_scene.command_manager.undo_stack.append(command)
            
        QGraphicsItem.mouseReleaseEvent(
            cast(QGraphicsItem, self),
            event,
        )
        