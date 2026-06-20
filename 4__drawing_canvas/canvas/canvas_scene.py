from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtWidgets import QGraphicsSceneMouseEvent

from tools.tool_protocol import Tool
from tools.select_tool import SelectTool

class CanvasScene(QGraphicsScene):
    def __init__(self) -> None:
        super().__init__()

        self.active_tool: Tool | None = None

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