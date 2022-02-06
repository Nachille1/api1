import sys
import requests

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


class Ex(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)
        self.btn.clicked.connect(self.run)

    def run(self):
        api_server = 'http://static-maps.yandex.ru/1.x/'
        coords = self.coords.text().split(';')
        spn = self.spn.text()
        params = {
            'll': coords,
            'spn': spn,
            'l': 'map'
        }
        response = requests.get(api_server, params=params)
        map_file = 'map.png'
        with open(map_file, 'wb') as file:
            file.write(response.content)
        if response:
            pixmap = QPixmap(map_file)
            self.image.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.exit(app.exec())
