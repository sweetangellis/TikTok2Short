from PySide6.QtWidgets import (
    QMainWindow, QTabWidget, QVBoxLayout, QWidget, QLabel,
    QStatusBar, QMenuBar, QMenu, QMessageBox
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QTimer

# Import our tab classes
from gui.process_tab import ProcessTab
# The other tab imports will be uncommented as we implement them
# from gui.download_tab import DownloadTab
# from gui.metadata_tab import MetadataTab
# from gui.upload_tab import UploadTab

import logging
import os
logger = logging.getLogger("TikTok2YouTube.MainWindow")

class MainWindow(QMainWindow):
    """
    Main application window that hosts the tab interface and 
    coordinates between different components of the application.
    """
    
    def __init__(self, config):
        super().__init__()
        
        # Store configuration reference
        self.config = config
        
        # Set up window properties
        self.setWindowTitle("TikTok to YouTube Shorts Automation")
        self.setMinimumSize(1000, 700)  # Set a reasonable minimum size
        
        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget)
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_label = QLabel("Ready")
        self.status_bar.addWidget(self.status_label)
        
        # Create tabs (a mix of real and placeholder tabs until all are implemented)
        self.create_tabs()
        
        # Create menu bar with basic actions
        self.create_basic_menu()
        
        logger.info("Main window initialized")
    
    def create_tabs(self):
        """Create application tabs"""
        # Download tab (placeholder for now)
        download_tab = QWidget()
        download_layout = QVBoxLayout(download_tab)
        download_layout.addWidget(QLabel("Download Tab - Import and download TikTok videos"))
        self.tab_widget.addTab(download_tab, "Download")
        
        # Process tab (real implementation)
        self.process_tab = ProcessTab(self.config)
        self.tab_widget.addTab(self.process_tab, "Process")
        
        # Metadata tab (placeholder for now)
        metadata_tab = QWidget()
        metadata_layout = QVBoxLayout(metadata_tab)
        metadata_layout.addWidget(QLabel("Metadata Tab - Edit titles, descriptions, and tags"))
        self.tab_widget.addTab(metadata_tab, "Metadata")
        
        # Upload tab (placeholder for now)
        upload_tab = QWidget()
        upload_layout = QVBoxLayout(upload_tab)
        upload_layout.addWidget(QLabel("Upload Tab - Schedule and manage uploads"))
        self.tab_widget.addTab(upload_tab, "Upload")
    
    def create_basic_menu(self):
        """Create a basic menu bar with essential actions"""
        menu_bar = self.menuBar()
        
        # File menu
        file_menu = menu_bar.addMenu("&File")
        
        # Exit action
        exit_action = QAction("&Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menu_bar.addMenu("&Help")
        
        # About action
        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def show_about(self):
        """Show about dialog with information about the application"""
        QMessageBox.about(
            self,
            "About TikTok to YouTube Shorts Automation",
            "This application automates the process of converting TikTok content to YouTube Shorts.\n\n"
            "Features:\n"
            "• Video processing with FFmpeg\n"
            "• Metadata editing\n"
            "• YouTube upload management\n\n"
            "Version: 1.0.0"
        )