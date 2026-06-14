from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QDragEnterEvent, QDropEvent
import sys

class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        print("drag enter")
        event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        print("drop")
        event.acceptProposedAction()

app = QApplication(sys.argv)

w = TestWidget()
w.resize(400, 400)
w.show()

app.exec()