from PySide6.QtWidgets import QTextEdit

class TextEditor(QTextEdit):
    def __init__(self):
        super().__init__()
        
        self.setPlaceholderText("Start typing here...")
        
        