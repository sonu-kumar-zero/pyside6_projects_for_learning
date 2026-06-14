from PySide6.QtWidgets import QMainWindow, QToolBar
from app.widgets.image_viewer import ImageViewer
from app.controllers.image_controller import ImageController
from PySide6.QtGui import QAction, QResizeEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.resize(1024, 720)
        
        self.viewer = ImageViewer()
        self.controller = ImageController(
            window=self,
            viewer=self.viewer,
            status_callback=self.update_status
        )
        
        self.setCentralWidget(self.viewer)
        
        self.create_actions()
        # self.create_menus()
        self.create_toolbar()
        self._connect_signals()
        self.statusBar()
    
    def _connect_signals(self):
        self.viewer.zoom_in_requested.connect(self.controller.zoom_in)
        self.viewer.zoom_out_requested.connect(self.controller.zoom_out)
        self.viewer.image_dropped.connect(self.controller.load_image)
    
    def create_actions(self):
        self.open_action = QAction("Open", self)
        self.zoom_in_action = QAction("Zoom In", self)
        self.zoom_out_action = QAction("Zoom Out", self)
        self.reset_zoom_action = QAction("Reset zoom", self)
        self.fit_action = QAction("Fit to Window", self)
        self.full_screen_action = QAction("Full Screen", self)
        
        self.open_action.triggered.connect(self.controller.open_image)
        self.zoom_in_action.triggered.connect(self.controller.zoom_in)
        self.zoom_out_action.triggered.connect(self.controller.zoom_out)
        self.reset_zoom_action.triggered.connect(self.controller.reset_zoom)
        self.fit_action.triggered.connect(self.controller.fit_to_window)
        self.full_screen_action.triggered.connect(self.controller.toggle_full_screen)
            
    def create_menus(self):
        file_menu = self.menuBar().addMenu("File")
        view_menu = self.menuBar().addMenu("View")
        
        file_menu.addAction(self.open_action)
        view_menu.addSeparator()
        view_menu.addAction(self.zoom_in_action)
        view_menu.addAction(self.zoom_out_action)
        view_menu.addSeparator()
        view_menu.addAction(self.fit_action)
        
    def create_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        
        toolbar.addAction(self.open_action)
        toolbar.addSeparator()
        toolbar.addAction(self.zoom_in_action)
        toolbar.addAction(self.zoom_out_action)
        toolbar.addAction(self.reset_zoom_action)
        toolbar.addSeparator()
        toolbar.addAction(self.fit_action)
        toolbar.addAction(self.full_screen_action)
        
    def resizeEvent(self, event:QResizeEvent):
        super().resizeEvent(event)
        if self.controller.state.fit_to_window:
            self.controller.fit_to_window()
    
    def update_status(self, text: str, ):
        self.statusBar().showMessage(text)