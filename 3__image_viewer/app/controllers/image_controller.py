from PySide6.QtWidgets import (
    QFileDialog,
    QMainWindow
)
from PySide6.QtGui import QPixmap
from app.widgets.image_viewer import ImageViewer
from app.models.image_state import ImageState
from pathlib import Path
from app.assets.constants import Constants
from typing import Callable


class ImageController:
    def __init__(self, window: QMainWindow, viewer: ImageViewer, status_callback: Callable[[str], None]):
        self.window = window
        self.viewer = viewer
        self.state = ImageState()
        self.status_callback = status_callback
        
    def open_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self.window,
            "",
            (
                "Image Files (*.png *.jpg *.jpeg *.bmp *.gif *.webp);;All Files (*)"
            ),
        )
        if not path:
            return
    
        self.load_image(path)
        
        
    def load_image(self, path: str):
        if not path:
            return
    
        pixmap = QPixmap(path)
        if pixmap.isNull():
            return
        
        self.state.current_file = Path(path)
        self.state.zoom_factor = Constants.DEFAULT_ZOOM
        self.state.fit_to_window = False
        
        self.viewer.set_pixmap(pixmap)
        self.fit_to_window()
        self.update_status_bar()
    
    def zoom_in(self):
        if not self.viewer.original_pixmap:
            return
    
        self.state.fit_to_window = False
        self.state.zoom_factor *= Constants.ZOOM_IN_FACTOR
        self.state.zoom_factor = min(self.state.zoom_factor, Constants.MAX_ZOOM)
        
        self.viewer.scale_image(
            self.state.zoom_factor
        )
        self.update_status_bar()
        
    def zoom_out(self):
        if not self.viewer.original_pixmap:
            return
    
        self.state.fit_to_window = False
        self.state.zoom_factor *= Constants.ZOOM_OUT_FACTOR
        self.state.zoom_factor = max(self.state.zoom_factor, Constants.MIN_ZOOM)
        
        self.viewer.scale_image(
            self.state.zoom_factor
        )
        self.update_status_bar()
        
    def fit_to_window(self):
        if not self.viewer.original_pixmap:
            return
    
        self.state.fit_to_window = True
        self.state.zoom_factor = Constants.DEFAULT_ZOOM
        
        self.viewer.fit_image()
        self.update_status_bar()
        
    def toggle_full_screen(self):
        if self.window.isMaximized():
            self.window.showNormal()
        else:
            self.window.showMaximized()
    
    def reset_zoom(self):
        if not self.viewer.original_pixmap:
            return
    
        self.state.fit_to_window = False
        self.state.zoom_factor = Constants.DEFAULT_ZOOM
        
        self.viewer.scale_image(
            self.state.zoom_factor
        )
        self.update_status_bar()

    def update_status_bar(self):
        if not self.viewer.original_pixmap:
            self.status_callback("")
            return
        
        pixmap = self.viewer.original_pixmap
        
        width = pixmap.width()
        height = pixmap.height()
        
        zoom = int(self.state.zoom_factor * 100)
        file_name = self.state.current_file.name if self.state.current_file else "No file"
        
        self.status_callback(f"{file_name} | {width}x{height} - {zoom}%")