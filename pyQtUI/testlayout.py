import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,  QVBoxLayout
import searchbar

testlist = ["abuse", "adult", "drama", "drain",
            "enemy", "entry", "catch", "could", "would"]


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("pyReferences")
        self.setFixedHeight(66)

        layout = QVBoxLayout()

        self.bucket = QWidget()

        self.searchbar = searchbar.SearchBar()

        layout.addWidget(self.searchbar)
        layout.addWidget(self.bucket)
        # layout.addWidget(self.btnSearch, stretch=1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

print(window.bucket)

app.exec()
