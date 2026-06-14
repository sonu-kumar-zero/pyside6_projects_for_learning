import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtCore import Qt

class CounterWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Counter")
        
        self.counter = 0
        
        self._ui_setup()
    
    def _ui_setup(self):
        self.label = QLabel(str(self.counter))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 24px;")
        
        self.incrementButton = QPushButton("Size Increment")
        self.incrementButton.clicked.connect(self.size_increment)
        self.decrementButton = QPushButton("Size Decrement")
        self.decrementButton.clicked.connect(self.size_decrement)
        
        self.resetButton = QPushButton("Reset")
        self.resetButton.clicked.connect(self.reset_counter)
        
        root_window_layout = QVBoxLayout()
        self.setLayout(root_window_layout)
        
        root_window_layout.addWidget(self.label, stretch=1)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.incrementButton)
        button_layout.addWidget(self.decrementButton)
        
        
        root_window_layout.addLayout(button_layout)
        
        root_window_layout.addWidget(self.resetButton)
    
    def label_update(self):
        self.label.setText(str(self.counter))
        
    def size_increment(self):
        self.counter += 1
        self.label_update()
    
    def size_decrement(self):
        if self.counter > 0:
            self.counter -= 1
            self.label_update()
            
    def reset_counter(self):
        self.counter = 0
        self.label_update()

app = QApplication(sys.argv)

window = CounterWindow()
window.show()

sys.exit(app.exec())