"""
The MIT License (MIT)

Copyright (c) 2025 bensaida011

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from PySide6 import QtCore , QtWidgets, QtGui
from generator import password_gen


class Mywidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)




        self.label1 = QtWidgets.QLabel("Password Generator")
        self.label1.setFont(font)
        self.label1.adjustSize()
        self.text_copy =QtWidgets.QLineEdit("")

        self.button_generate = QtWidgets.QPushButton("Generate")
        self.button_generate.setStyleSheet('background-color: green')
        self.button_exit = QtWidgets.QPushButton("Exit")
        self.button_exit.setStyleSheet('background-color: red')

        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.text_copy)
        self.layout.addWidget(self.button_generate)
        self.layout.addWidget(self.button_exit)

        self.button_generate.clicked.connect(self.generate_password)
        self.button_exit.clicked.connect(self.exit_button)

        self.ErrorMessage = QtWidgets.QErrorMessage(self)


    @QtCore.Slot()
    def generate_password(self):
        password = password_gen(16)
        self.text_copy.setText(password)


    def exit_button(self):
        QtCore.QCoreApplication.exit(0)