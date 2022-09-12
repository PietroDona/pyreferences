
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit,  QSizePolicy


class SearchBar(QWidget):

    def __init__(self) -> None:
        super(QWidget, self).__init__()

        layout = QHBoxLayout()

        self.txtSearch = QLineEdit()
        self.txtSearch.setFont(QFont('Arial', 14))
        self.txtSearch.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.txtSearch.setMinimumWidth(400)

        icon = QIcon("assets/search.png")
        # add action to line edit
        self.txtSearch.addAction(
            icon, self.txtSearch.TrailingPosition)

        layout.addWidget(self.txtSearch)
        # layout.addWidget(self.btnSearch, stretch=1)

        self.setLayout(layout)
