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

        # Create a menu bar with a "Home" action
        self.menuBar = QMenuBar()
        self.actionNew = QAction("Home", self)
        self.menuBar.addAction(self.actionNew)
        self.actionNew.triggered.connect(self.go_home)

        self.actionNew = QAction("Resources", self)
        self.menuBar.addAction(self.actionNew)
        self.actionNew.triggered.connect(self.resources)


        self.fileMenu = self.menuBar.addMenu("More")
        self.actionNew = QAction("Help", self)
        self.fileMenu.addAction(self.actionNew)
        self.actionNew.triggered.connect(self.help)
                                         
        self.actionNew = QAction("About", self)
        self.fileMenu.addAction(self.actionNew)
        self.actionNew.triggered.connect(self.about)

        # Set the menu bar for the main window
        self.setMenuBar(self.menuBar)

        # Create a web browser widget using QWebEngineView
        self.browser = QWebEngineView()

        # Set the browser widget as the central widget of the main window
        self.setCentralWidget(self.browser)

        # Set the window size to 1600 x 400
        #self.setGeometry(0, 0, 710, 390)

        # Get the current directory of the program and set the path to the HTML file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "resources", "index.html")

        # Load the HTML file into the browser widget
        self.browser.load(QUrl.fromLocalFile(file_path))

        # Show the main window
        self.show()

    def go_home(self):
        # Get the current directory of the program and set the path to the HTML file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "resources", "index.html")

        # Load the HTML file into the browser widget
        self.browser.load(QUrl.fromLocalFile(file_path))

    def resources(self):
        # Get the current directory of the program and set the path to the HTML file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "resources", "resources.html")

        # Load the HTML file into the browser widget
        self.browser.load(QUrl.fromLocalFile(file_path))
    
    def help(self):
        # Get the current directory of the program and set the path to the HTML file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "resources", "help.html")

        # Load the HTML file into the browser widget
        self.browser.load(QUrl.fromLocalFile(file_path))

    def about(self):
        # Get the current directory of the program and set the path to the HTML file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "resources", "about.html")

        # Load the HTML file into the browser widget
        self.browser.load(QUrl.fromLocalFile(file_path))


# Create a QApplication instance, a MyWebBrowser instance, and execute the application
app = QApplication([])
window = MyWebBrowser()
app.exec_()
