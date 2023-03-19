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

        # Set the menu bar for the main window
        self.setMenuBar(self.menuBar)

        # Create a web browser widget using QWebEngineView
        self.browser = QWebEngineView()

        # Set the browser widget as the central widget of the main window
        self.setCentralWidget(self.browser)

        # Set the window size to 1600 x 400
        self.setGeometry(0, 0, 710, 390)

        # Load the HTML file into the browser widget
        self.browser.setUrl(QUrl("https://google.com"))

        # Show the main window
        self.show()

    def go_home(self):
        # Load the HTML file into the browser widget
        self.browser.setUrl(QUrl("https://google.com"))


# Create a QApplication instance, a MyWebBrowser instance, and execute the application
app = QApplication([])
window = MyWebBrowser()
app.exec_()
