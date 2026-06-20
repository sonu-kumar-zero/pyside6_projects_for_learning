from PySide6.QtWidgets import QGraphicsView

from canvas.canvas_scene import CanvasScene


class CanvasView(QGraphicsView):
    def __init__(
        self,
        scene: CanvasScene,
    ) -> None:
        super().__init__(scene)

        self.setMouseTracking(True)