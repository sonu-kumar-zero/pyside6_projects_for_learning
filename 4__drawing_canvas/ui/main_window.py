from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
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

        self.scene.set_tool(
            self.select_tool
        )

    def _create_toolbar(self) -> None:
        toolbar = QToolBar("Tools")

        toolbar.setMovable(False)

        self.addToolBar(
            Qt.ToolBarArea.TopToolBarArea,
            toolbar,
        )

        select_action = QAction(
            "Select",
            self,
        )

        rectangle_action = QAction(
            "Rectangle",
            self,
        )

        ellipse_action = QAction(
            "Ellipse",
            self,
        )

        select_action.triggered.connect(
            lambda: self.scene.set_tool(
                self.select_tool
            )
        )

        rectangle_action.triggered.connect(
            lambda: self.scene.set_tool(
                self.rectangle_tool
            )
        )

        ellipse_action.triggered.connect(
            lambda: self.scene.set_tool(
                self.ellipse_tool
            )
        )

        toolbar.addAction(select_action)
        toolbar.addAction(rectangle_action)
        toolbar.addAction(ellipse_action)