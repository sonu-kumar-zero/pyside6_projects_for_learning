from PySide6.QtWidgets import QGraphicsView 
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QWheelEvent, QMouseEvent 
from canvas.canvas_scene import CanvasScene


class CanvasView(QGraphicsView):
    ZOOM_FACTOR = 1.15
    drag_mode = False
    def __init__(
        self,
        scene: CanvasScene,
    ) -> None:
        super().__init__(scene)

        self.setMouseTracking(True)
        
        # Disable scrollbars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # zoom around mouse position
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        
        # Enable antialiasing for smoother rendering
        self.setRenderHints(
            self.renderHints() | 
            QPainter.RenderHint.Antialiasing | 
            QPainter.RenderHint.SmoothPixmapTransform
        )
        
        # disable default drag mode
        self.drag_disable()
        self._pan_start = QPoint()

    
    def zoom_in(self) -> None:
        self.scale(
            self.ZOOM_FACTOR,
            self.ZOOM_FACTOR,
        )
    
    def zoom_out(self) -> None:
        self.scale(
            1 / self.ZOOM_FACTOR,
            1 / self.ZOOM_FACTOR,
        )
    
    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.angleDelta().y() > 0:
                self.zoom_in()
            else:
                self.zoom_out()
            event.accept()
            return

        super().wheelEvent(event)
    
    def drag_enable(self) -> None:
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
    
    def drag_disable(self) -> None:
        self.setDragMode(QGraphicsView.DragMode.NoDrag)

    def toggle_drag(self) -> None:
        if not self.drag_mode:
            self.drag_enable()
            self.drag_mode = True
        else:
            self.drag_disable()
            self.drag_mode = False
        
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.MiddleButton:
            self.drag_mode = True
            self.drag_enable()
            self._pan_start = event.pos()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()
            return
        
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.drag_mode:
            delta = event.pos() - self._pan_start
            self._pan_start = event.pos()
            
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - delta.x()
            )
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - delta.y()
            )
            
            event.accept()
            return
        
        super().mouseMoveEvent(event)
        
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.MiddleButton:
            self.drag_mode = False
            self.drag_disable()
            self.setCursor(Qt.CursorShape.ArrowCursor)
            event.accept()
            return
        
        super().mouseReleaseEvent(event)