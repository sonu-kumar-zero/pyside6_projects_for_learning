from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtWidgets import QGraphicsSceneMouseEvent
from tools.tool_protocol import Tool


class SelectTool(Tool):
    def mouse_press(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        scene.clearSelection()

        item = scene.itemAt(
            event.scenePos(),
            scene.views()[0].transform(),
        )

        if item is not None:
            item.setSelected(True)

    def mouse_move(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        pass

    def mouse_release(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        pass