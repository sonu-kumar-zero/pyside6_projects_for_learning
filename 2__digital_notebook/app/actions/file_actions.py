from PySide6.QtWidgets import ( QFileDialog )
from PySide6.QtWidgets import (
    QMainWindow,
)

from app.widgets.text_editor import (
    TextEditor,
)

from app.services.file_service import (
    FileService,
)
from pathlib import Path


class FileActions:
    def __init__(self, window: QMainWindow, editor: TextEditor, file_services: FileService):
        self.window = window
        self.editor = editor
        self.file_services = file_services
        
        self.current_file = None
    
    def new_document(self):
        self.editor.clear()
        self.current_file = None
        
    def open_document(self):
        path, _ = QFileDialog.getOpenFileName(
            self.window, "Open File", "", "Text Files (*.txt);;All Files (*)"
        )
        if not path:
            return
        
        content:str = self.file_services.load_file(path)
        
        self.editor.setPlainText(content)
        self.current_file = path
        
    def save_document(self):
        if self.current_file is None:
            path, _ = QFileDialog.getSaveFileName(
                self.window, "Save File", "", "Text Files (*.txt);;All Files (*)"
            )
            if not path:
                return
            
            path = Path(path)
            
            if not path.suffix:
                path = path.with_suffix(".txt")
            
            self.current_file = path
        
        self.current_file = Path(self.current_file)
        
        self.file_services.save_file(
            self.current_file.as_posix(), 
            self.editor.toPlainText()
        )