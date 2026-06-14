from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QScrollArea,
    QVBoxLayout,
)
from PySide6.QtGui import QPixmap, QWheelEvent, QDragEnterEvent, QDropEvent
from PySide6.QtCore import Qt, Signal
from pathlib import Path
from app.assets.constants import VALID_IMAGE_EXTENSIONS

class ImageViewer(QWidget):
    zoom_in_requested = Signal()
    zoom_out_requested = Signal()
    image_dropped = Signal(str)
    def __init__(self):
        super().__init__()
    
        
        self.original_pixmap: QPixmap | None = None

        self.image_label = QLabel()
        
        self._setup_ui()
    
    def _setup_ui(self):
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.image_label)
        
        self.scroll_area.setAcceptDrops(True)
        self.image_label.setAcceptDrops(True)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)
        
    def set_pixmap(self, pixmap: QPixmap):
        self.original_pixmap = pixmap
        self.image_label.setPixmap(pixmap)
        
    def scale_image(self, factor: float):
        if not self.original_pixmap:
            return 
        
        size = self.scroll_area.viewport().size() * factor
        scaled = self.original_pixmap.scaled(
            size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        
        self.image_label.setPixmap(scaled)
    
    def fit_image(self):
        if not self.original_pixmap:
            return
        
        scaled = self.original_pixmap.scaled(
            self.scroll_area.viewport().size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        
        self.image_label.setPixmap(scaled)
        
    def wheelEvent(self, event: QWheelEvent):
        modifiers = event.modifiers()
        
        if modifiers & Qt.KeyboardModifier.ControlModifier:
            if event.angleDelta().y() > 0:
                self.zoom_in_requested.emit()
            else:
                self.zoom_out_requested.emit()
            
            event.accept()
            return
    
        super().wheelEvent(event)    
        
    def dragEnterEvent(self, event: QDragEnterEvent):
        print("Drag Enter Event")
        if not event.mimeData().hasUrls():
            event.ignore()
            return
    
        urls = event.mimeData().urls()
        
        if not urls:
            event.ignore()
            return
        
        file_path = urls[0].toLocalFile()
        
        suffix = (Path(file_path).suffix or "").lower()
        if suffix not in VALID_IMAGE_EXTENSIONS:
            event.ignore()
            return
        else:
            event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        print("Drop Event")
        urls = event.mimeData().urls()
        
        if not urls:
            event.ignore()
            return
        
        file_path = urls[0].toLocalFile()
        
        suffix = (Path(file_path).suffix or "").lower()
        if suffix not in VALID_IMAGE_EXTENSIONS:
            event.ignore()
            return
        
        self.image_dropped.emit(file_path)
        
        event.acceptProposedAction()
