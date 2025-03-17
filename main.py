from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_Calculator2
class Widget(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.ui = Ui_Calculator2()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.proverka)
    def calculator(self):
        # Отримуємо вхідні дінні
        text_znak = self.ui.znak.currentText()
        text1 = self.ui.num1.text()
        text2 = self.ui.num2.text()

        try: #на випадок якщо введені не числа
            number1 = float(text1)
            number2 = float(text2)
            # Рахування
            if text_znak == "+":
                result = number1 + number2
            elif text_znak == "-":
                result = number1 - number2
            elif text_znak == "*":
                result = number1 * number2
            elif text_znak == "/":
                if number2 != 0:
                    result = number1 / number2
                else:
                    self.ui.label.setText("Помилка: не можна поділити на 0")
                    return
            else:
                self.ui.label.setText("Помилка: незнайомий знак")
                return

            # результат
            self.ui.label.setText(str(result))

        except ValueError:
            self.ui.label.setText("Помилка: Введіть числа")
    def proverka(self):
        if self.ui.num1.text().strip() and self.ui.num2.text().strip(): #strip() прибирає пробіли
            self.calculator()
        else:
            self.ui.label.setText("Помилка: заповніть обидва поля")

   
        
    
        
app = QApplication([])
ex = Widget()
ex.show()



app.exec_()