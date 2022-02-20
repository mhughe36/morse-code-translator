import sys
from tkinter import E
from PyQt6 import QtCore
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets

class MorseWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.message = 'Sample'

        self.MORSEDICTIONARY = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

        self.window_length = 600
        self.window_height = 600

        #initialize buttons/labels
        self.encrypt = QPushButton(self)
        self.decrypt = QPushButton(self)
        self.entermorse = QLabel(self)
        self.entertext = QLabel(self)
        self.outmorse = QLabel(self)
        self.outtext = QLabel(self)
        self.encryptmsg = QLabel(self)
        self.decryptmsg = QLabel(self)
        self.inputmorse = QLineEdit(self)
        self.inputtext = QLineEdit(self)

        self.encrypt.setText('Encrypt')
        self.decrypt.setText('Decrypt')
        self.entermorse.setText('Morse: ')
        self.entertext.setText('Text: ')
        self.outmorse.setText('... .- -- .--. .-.. .')
        self.outtext.setText('Sample')
        self.encryptmsg.setText('Morse: ')
        self.decryptmsg.setText('Text: ')

        self.encrypt.setGeometry(220, 30, 60, 40)
        self.decrypt.setGeometry(550, 30, 60, 40)
        self.entertext.setGeometry(20, 30, 60, 30)
        self.entermorse.setGeometry(320, 30, 60, 30)
        self.outmorse.setGeometry(65, 200, 100, 20)
        self.outtext.setGeometry(300, 200, 200, 20)
        self.encryptmsg.setGeometry(20, 200, 50, 20)
        self.decryptmsg.setGeometry(270, 200, 50, 20)
        self.inputtext.setGeometry(100, 30, 100, 30)
        self.inputmorse.setGeometry(350, 30, 100, 30)

        self.encrypt.clicked.connect(self.encryptclicked)


        self.show()

    def encryptclicked(self):
        self.message = self.inputtext.text()
        self.outmorse.setText(self.enc())

    def enc(self):
        count = ''
        for letter in self.message:
            if letter != ' ':
                count +=self.MORSEDICTIONARY[letter] + ' '
            else:
                count += ' '

        return count
            
    


    def set_widget(self, widget):
        self.widget = widget



if __name__ == '__main__':
    # initialize QT application
    app = QApplication(sys.argv)

    main_window = MorseWindow()
    widget = QtWidgets.QStackedWidget()
    main_window.set_widget(widget)
    main_window.initUI()

    # pull both into the widget and run
    widget.setWindowTitle("Morse Code")
    widget.setGeometry(0, 0, 840, 660)
    widget.addWidget(main_window)
    widget.show()
    sys.exit(app.exec())