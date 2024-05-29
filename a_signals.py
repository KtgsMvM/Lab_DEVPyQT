"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets
from formA import Ui_radioButton_2

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_radioButton_2()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.mirror)
        self.ui.lineEditInput.textEdited.connect(self.mirror)
        self.ui.lineEditMirror.textChanged.connect(lambda x: self.ui.lineEdit.setText(x[::-1]))
        self.ui.radioButton.toggled.connect(self.my_func)
    def mirror(self):
        input_text = self.ui.lineEditInput.text()[::-1]
        self.ui.lineEditMirror.setText(input_text)


    def my_func(self, param):
        if param == True:
            self.ui.lineEdit.setText("Радио включено")
        else:
            self.ui.lineEdit.setText("Радио выключено")

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()


# from PySide6.QtWidgets import QPushButton
#
# button = QPushButton('Кнопка', self)
# button.setGeometry(10, 10, 100, 30)
# button.setStyleSheet('background-color: red; color: white;')