from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtWidgets import QGraphicsSceneMouseEvent

from tools.tool_protocol import Tool
from tools.select_tool import SelectTool

from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import QRect, QRectF

class CanvasScene(QGraphicsScene):
    MAJOR_GRID_SIZE: int = 125
    MINOR_GRID_SIZE = 25
    def __init__(self) -> None:
        super().__init__()

        self.active_tool: Tool | None = None
        
        self.setSceneRect(
            -100_000,
            -100_000,
            200_000,
            200_000,
        )

    def set_tool(
        self,
        tool: Tool,
    ) -> None:
        self.active_tool = tool

    def mousePressEvent(
        self,
        event: QGraphicsSceneMouseEvent,
    ) -> None:
        if self.active_tool is None:
            super().mousePressEvent(event)
            return

        self.active_tool.mouse_press(event, self)
        
        if isinstance(self.active_tool, SelectTool):
            super().mousePressEvent(event)
        else:
            event.accept()

    def mouseMoveEvent(
        self,
        event: QGraphicsSceneMouseEvent,
    ) -> None:
        if self.active_tool is None:
            super().mouseMoveEvent(event)
            return
        
        self.active_tool.mouse_move(event, self)
        
        if isinstance(self.active_tool, SelectTool):
            super().mouseMoveEvent(event)
        else:
            event.accept()
        
    def mouseReleaseEvent(
        self,
        event: QGraphicsSceneMouseEvent,
    ) -> None:
        
        if self.active_tool is None:
            super().mouseReleaseEvent(event)
            return
        
        self.active_tool.mouse_release(event, self)
        
        if isinstance(self.active_tool, SelectTool):
            super().mouseReleaseEvent(event)
        else:
            event.accept()
        
    def drawBackground(self, painter: QPainter, rect: QRectF | QRect) -> None:
        super().drawBackground(painter, rect)
        
        left:int = int(rect.left())
        top:int = int(rect.top())
        right:int = int(rect.right())
        bottom:int = int(rect.bottom())
        
        first_x:int = left - (
            left % self.MINOR_GRID_SIZE
        )
        first_y:int = top - (
            top % self.MINOR_GRID_SIZE
        )
        
        minor_pen: QPen = QPen(QColor(235, 235, 235), 1)
        major_pen: QPen = QPen(QColor(200, 200, 200), 1)
        
        # vertical lines
        x:int = first_x
        while x < right:
            if x % self.MAJOR_GRID_SIZE == 0:
                painter.setPen(major_pen)
            else:
                painter.setPen(minor_pen)
                
            painter.drawLine(
                x,
                top,
                x,
                bottom,
            )
            
            x += self.MINOR_GRID_SIZE
        
        # horizontal lines
        y:int = first_y
        while y < bottom:
            if y % self.MAJOR_GRID_SIZE == 0:
                painter.setPen(major_pen)
            else:
                painter.setPen(minor_pen)
                
            painter.drawLine(
                left,
                y,
                right,
                y,
            )
            
            y += self.MINOR_GRID_SIZE