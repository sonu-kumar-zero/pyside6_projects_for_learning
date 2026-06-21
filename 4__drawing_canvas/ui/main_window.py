from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QGraphicsItem
)

from canvas.canvas_scene import CanvasScene
from canvas.canvas_view import CanvasView

from tools.select_tool import SelectTool
from tools.rectangle_tool import RectangleTool
from tools.ellipse_tool import EllipseTool


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Drawing Canvas")

        self.scene = CanvasScene()
        self.view = CanvasView(self.scene)

        self.setCentralWidget(self.view)

        self.select_tool = SelectTool()
        self.rectangle_tool = RectangleTool()
        self.ellipse_tool = EllipseTool()

        self._create_toolbar()

    def _create_toolbar(self) -> None:
        toolbar = QToolBar("Tools")

        toolbar.setMovable(False)

        self.addToolBar(
            Qt.ToolBarArea.TopToolBarArea,
            toolbar,
        )

        select_action = QAction("Select", self)
        select_action.triggered.connect(lambda: self.scene.set_tool(self.select_tool))
        select_action.setShortcut(QKeySequence("S"))

        rectangle_action = QAction("Rectangle", self)
        rectangle_action.triggered.connect(lambda: self.scene.set_tool(self.rectangle_tool))
        rectangle_action.setShortcut(QKeySequence("Shift+R"))
        
        ellipse_action = QAction("Ellipse", self)
        ellipse_action.triggered.connect(lambda: self.scene.set_tool(self.ellipse_tool))
        ellipse_action.setShortcut(QKeySequence("Shift+E"))

        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(lambda: self.delete_selected_items())
        delete_action.setShortcut(QKeySequence.StandardKey.Delete)

        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(lambda: self.scene.clear())
        clear_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        
        zoom_in_action = QAction("Zoom In", self)
        zoom_in_action.triggered.connect(lambda: self.view.zoom_in())
        zoom_in_action.setShortcut(QKeySequence.StandardKey.ZoomIn)
        
        zoom_out_action = QAction("Zoom Out", self)
        zoom_out_action.triggered.connect(lambda: self.view.zoom_out())
        zoom_out_action.setShortcut(QKeySequence.StandardKey.ZoomOut)
        
        drag_action = QAction("Drag", self)
        drag_action.triggered.connect(lambda: self.view.toggle_drag())
        drag_action.setShortcut

        toolbar.addAction(select_action)
        toolbar.addSeparator()
        toolbar.addAction(rectangle_action)
        toolbar.addAction(ellipse_action)
        toolbar.addSeparator()
        toolbar.addAction(delete_action)
        toolbar.addAction(clear_action)
        toolbar.addSeparator()
        toolbar.addAction(zoom_in_action)
        toolbar.addAction(zoom_out_action)
        toolbar.addSeparator()
        toolbar.addAction(drag_action)
        
    def delete_selected_items(self) -> None:
        items: list[QGraphicsItem] = self.scene.selectedItems()
        for item in items:
            self.scene.removeItem(item)