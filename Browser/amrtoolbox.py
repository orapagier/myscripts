from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import os


class MyWebBrowser(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        # Set the title of the main window
        self.setWindowTitle("AMR TOOLBOX")

        # Create a vertical layout and a horizontal layout
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        # Create a menu bar with a "Home" action
        self.menuBar = QMenuBar()
        self.actionNew = QAction("Home", self)
        self.menuBar.addAction(self.actionNew)
        self.actionNew.triggered.connect(self.go_home)

        # Set the menu bar for the main window
        self.setMenuBar(self.menuBar)

        # Create a web browser widget using QWebEngineView
        self.browser = QWebEngineView()

        # Add the browser widget to the layout
        self.layout.addWidget(self.browser)

        # Get the current directory of the program and set the path to the HTML file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "resources", "index.html")

        # Load the HTML file into the browser widget
        self.browser.load(QUrl.fromLocalFile(file_path))

        # Set the layout of the main window and show it
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
        self.show()

    def go_home(self):
        # Get the current directory of the program and set the path to the HTML file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "resources", "index.html")

        # Load the HTML file into the browser widget
        self.browser.load(QUrl.fromLocalFile(file_path))


# Create a QApplication instance, a MyWebBrowser instance, and execute the application
app = QApplication([])
window = MyWebBrowser()
app.exec_()
