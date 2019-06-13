from db import DBHandler
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QMessageBox, QAction ,QLineEdit
import PyQt5.QtWidgets


class Login(QMainWindow):
    def __init__(self):
        super().__init__()

    def createPage(self):
        self.resize(350, 350)
        self.move(200, 200)

        self.layout = QVBoxLayout()
        self.setWindowTitle("Welcome Buddy!")
        self.setLayout(self.layout)


        username = PyQt5.QtWidgets.QTextEdit(self)
        username.resize(300, 40)
        username.setFontPointSize(20)
        username.move(25, 50)

        usernameText = PyQt5.QtWidgets.QTextBrowser(self)
        usernameText.setText("username")
        usernameText.resize(300,30)
        usernameText.move(25,20)

        passwordText = PyQt5.QtWidgets.QTextBrowser(self)
        passwordText.setText("password")
        passwordText.resize(300,30)
        passwordText.move(25,120)

        password = PyQt5.QtWidgets.QTextEdit(self)
        password.resize(300, 40)
        password.setFontPointSize(20)
        password.move(25, 150)

        login = QPushButton("Login", self)
        login.resize(300, 40)
        login.move(25, 200)

        register = QPushButton("Register", self)
        register.resize(300, 40)
        register.move(25, 250)

        quit = QAction("Quit", self)
        quit.triggered.connect(self.close)

        menubar = self.menuBar()
        fmenu = menubar.addMenu("File")
        fmenu.addAction(quit)

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class Registering(QMainWindow):
    def __init__(self):
        super().__init__()

    def createPage(self):
        self.resize(350, 350)
        self.move(300, 300)

        self.layout = QVBoxLayout()
        self.setWindowTitle("Fill the blanks :)!")
        self.setLayout(self.layout)

        nameText = PyQt5.QtWidgets.QTextBrowser(self)
        nameText.setText("name")
        nameText.resize(300, 30)
        nameText.move(25, 10)

        name = PyQt5.QtWidgets.QTextEdit(self)
        name.resize(300, 40)
        name.setFontPointSize(20)
        name.move(25, 40)

        phoneText = PyQt5.QtWidgets.QTextBrowser(self)
        phoneText.setText("Phone")
        phoneText.resize(300, 30)
        phoneText.move(25, 80)

        phone = PyQt5.QtWidgets.QTextEdit(self)
        phone.resize(300, 40)
        phone.setFontPointSize(20)
        phone.move(25, 110)

        usernameText = PyQt5.QtWidgets.QTextBrowser(self)
        usernameText.setText("username")
        usernameText.resize(300, 30)
        usernameText.move(25, 150)

        username = PyQt5.QtWidgets.QTextEdit(self)
        username.resize(300, 40)
        username.setFontPointSize(20)
        username.move(25, 180)

        passwordText = PyQt5.QtWidgets.QTextBrowser(self)
        passwordText.setText("username")
        passwordText.resize(300, 30)
        passwordText.move(25, 220)

        password = PyQt5.QtWidgets.QTextEdit(self)
        password.resize(300, 40)
        password.setFontPointSize(20)
        password.move(25, 250)

        register = QPushButton("Register", self)
        register.resize(300, 40)
        register.move(25, 300)

        quit = QAction("Quit", self)
        quit.triggered.connect(self.close)

        menubar = self.menuBar()
        fmenu = menubar.addMenu("File")
        fmenu.addAction(quit)

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()




app = QApplication(sys.argv)

window = Login()
window.createPage()
window.show()

reg = Registering()
reg.createPage()
reg.show()

sys.exit(app.exec_())


