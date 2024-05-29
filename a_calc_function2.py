from PySide6 import QtWidgets
from form_calc2 import Ui_MainWindow

class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_0.clicked.connect(lambda: self.add_to_line_edit("0"))
        self.ui.pushButton_1.clicked.connect(lambda: self.add_to_line_edit("1"))
        self.ui.pushButton_2.clicked.connect(lambda: self.add_to_line_edit("2"))
        self.ui.pushButton_3.clicked.connect(lambda: self.add_to_line_edit("3"))
        self.ui.pushButton_4.clicked.connect(lambda: self.add_to_line_edit("4"))
        self.ui.pushButton_5.clicked.connect(lambda: self.add_to_line_edit("5"))
        self.ui.pushButton_6.clicked.connect(lambda: self.add_to_line_edit("6"))
        self.ui.pushButton_7.clicked.connect(lambda: self.add_to_line_edit("7"))
        self.ui.pushButton_8.clicked.connect(lambda: self.add_to_line_edit("8"))
        self.ui.pushButton_9.clicked.connect(lambda: self.add_to_line_edit("9"))
        self.ui.pushButton_add.clicked.connect(lambda: self.add_to_line_edit("+"))
        self.ui.pushButton_subtract.clicked.connect(lambda: self.add_to_line_edit("-"))
        self.ui.pushButton_multipl.clicked.connect(lambda: self.add_to_line_edit("*"))
        self.ui.pushButton_division.clicked.connect(lambda: self.add_to_line_edit("/"))
        self.ui.pushButton_comma.clicked.connect(lambda: self.add_to_line_edit(","))
        self.ui.pushButton_result.clicked.connect(self.solve)

# строка привести к int или использовать словарь?
# как отобразить действия - для каждого отдельную функцию
# кнопки с действиями не отображаются в дисплее, а вызывают соотв. действию функцию
# при нажатии на = функция вычисляется и отображает результат в дисплей

    def add_to_line_edit(self, number):
        self.ui.lineEditDisplay.setText(self.ui.lineEditDisplay.text() + number)

    def solve(self):
        result = eval(self.ui.lineEditDisplay.text())
        self.ui.lineEditDisplay.setText(str(result))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()