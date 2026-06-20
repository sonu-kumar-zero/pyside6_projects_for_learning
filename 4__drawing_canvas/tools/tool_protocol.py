from typing import Protocol

from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsSceneMouseEvent,
)


class Tool(Protocol):
    def mouse_press(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None: ...

    def mouse_move(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None: ...

    def mouse_release(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None: ...