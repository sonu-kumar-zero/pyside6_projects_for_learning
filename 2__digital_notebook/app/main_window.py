from PySide6.QtWidgets import (
    QMainWindow,
)

from app.widgets.text_editor import (
    TextEditor,
)

from app.services.file_service import (
    FileService,
)

from app.actions.file_actions import (
    FileActions,
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Digital Notebook"
        )

        self.resize(900, 700)

        self.editor = TextEditor()

        self.setCentralWidget(
            self.editor
        )

        self.file_actions = FileActions(
            self,
            self.editor,
            FileService(),
        )

        self.create_menu()
        
    def create_menu(self):

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu(
            "File"
        )

        new_action = file_menu.addAction(
            "New"
        )

        open_action = file_menu.addAction(
            "Open"
        )

        save_action = file_menu.addAction(
            "Save"
        )

        new_action.triggered.connect(
            self.file_actions.new_document
        )

        open_action.triggered.connect(
            self.file_actions.open_document
        )

        save_action.triggered.connect(
            self.file_actions.save_document
        )