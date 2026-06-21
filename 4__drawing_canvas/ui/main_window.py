from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QGraphicsItem,
    QFileDialog,
)

from canvas.canvas_scene import CanvasScene
from canvas.canvas_view import CanvasView

from tools.select_tool import SelectTool
from tools.rectangle_tool import RectangleTool
from tools.ellipse_tool import EllipseTool

from commands.delete_item_command import DeleteItemCommand
from commands.clear_canvas_command import ClearCanvasCommand

from serialization.scene_serializer import SceneSerializer
from serialization.scene_deserializer import SceneDeserializer

from pathlib import Path

from clipboard.clipboard_manager import ClipboardManager
from items.base_item import BaseItem
from models.shape import ShapeData
from items.item_factory import ItemFactory
from commands.add_item_command import AddItemCommand

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
        
        self.clipboard_manager = ClipboardManager()

        self._create_toolbar()

    def _create_toolbar(self) -> None:
        toolbar = QToolBar("Tools")

        toolbar.setMovable(False)

        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)

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
        clear_action.triggered.connect(lambda: self.clear_canvas())
        clear_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        
        zoom_in_action = QAction("Zoom In", self)
        zoom_in_action.triggered.connect(lambda: self.view.zoom_in())
        zoom_in_action.setShortcut(QKeySequence.StandardKey.ZoomIn)
        
        zoom_out_action = QAction("Zoom Out", self)
        zoom_out_action.triggered.connect(lambda: self.view.zoom_out())
        zoom_out_action.setShortcut(QKeySequence.StandardKey.ZoomOut)
        
        # drag_action = QAction("Drag", self)
        # drag_action.triggered.connect(lambda: self.view.toggle_drag())
        
        undo_action = QAction("Undo", self)
        undo_action.triggered.connect(lambda: self.scene.command_manager.undo())
        undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        
        redo_action = QAction("Redo", self)
        redo_action.triggered.connect(lambda: self.scene.command_manager.redo())
        redo_action.setShortcut(QKeySequence.StandardKey.Redo)

        save_action = QAction("Save", self)
        save_action.triggered.connect(lambda: self.save_scene())
        save_action.setShortcut(QKeySequence.StandardKey.Save)

        open_action = QAction("Open", self)
        open_action.triggered.connect(lambda: self.open_scene())
        open_action.setShortcut(QKeySequence.StandardKey.Open)

        copy_action = QAction("Copy", self)
        copy_action.triggered.connect(lambda: self.copy_selected_items())
        copy_action.setShortcut(QKeySequence.StandardKey.Copy)
        
        paste_action = QAction("Paste", self)
        paste_action.triggered.connect(lambda: self.paste_items())
        paste_action.setShortcut(QKeySequence.StandardKey.Paste)

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
        # toolbar.addAction(drag_action)
        # toolbar.addSeparator()
        toolbar.addAction(undo_action)
        toolbar.addAction(redo_action)
        toolbar.addSeparator()
        toolbar.addAction(save_action)
        toolbar.addAction(open_action)
        toolbar.addSeparator()
        toolbar.addAction(copy_action)
        toolbar.addAction(paste_action)
        toolbar.addSeparator()
        
        
    def delete_selected_items(self) -> None:
        items: list[QGraphicsItem] = self.scene.selectedItems()
        if not items:
            return
        
        command = DeleteItemCommand(self.scene, items)
        self.scene.command_manager.execute(command)
    
    def clear_canvas(self) -> None:
        command = ClearCanvasCommand(self.scene)
        self.scene.command_manager.execute(command)


    def save_scene(self) -> None:
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Scene", "", "JSON Files (*.json)")
        
        if not file_path:
            return
        
        file_path = Path(file_path)
        if file_path.suffix != ".json":
            file_path = file_path.with_suffix(".json")
        
        SceneSerializer.save(self.scene, file_path)
    
    def open_scene(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Scene", "", "JSON Files (*.json)")
        
        if not file_path:
            return
        
        file_path = Path(file_path)
        
        SceneDeserializer.load(self.scene, file_path)
        
    def copy_selected_items(self) -> None:
        self.clipboard_manager.data.clear()
        
        for item in self.scene.selectedItems():
            if not isinstance(item, BaseItem):
                continue

            shape_data = ShapeData.from_dict(item.to_dict())
                        
            self.clipboard_manager.data.append(shape_data)
            
    def paste_items(self) -> None:
        self.scene.clearSelection()
        for data in self.clipboard_manager.data:
            item = ItemFactory.create_item(data)
            item.setPos(data.pos_x + 20, data.pos_y + 20)  # Offset pasted items for visibility
            
            command = AddItemCommand(item, self.scene)
            self.scene.command_manager.execute(command)
            item.setSelected(True)  # Select the newly pasted item
              