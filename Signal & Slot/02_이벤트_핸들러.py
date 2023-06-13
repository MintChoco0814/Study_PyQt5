"""
    PyQt 에서 이벤트 처리를 할 때 사용되는 함수를
    이벤트 핸들러 라고 한다.

    'Big', 'Small' 버튼을 클릭 했을 때, 창의 크기가
    바뀌도록 하는 함수를 정의해보겠다.
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('Big', self)
        btn2 = QPushButton('Small', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)

        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)
        '''
            btn1과 btn2는 각각 resizeBig, resizeSmall 슬롯에 연결되어 있다.
            
        '''

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    def resizeBig(self):
        self.resize(400, 500)

    def resizeSmall(self):
        self.resize(200, 250)

    '''
        resizeBig() 메서드는 화면 크기를 가록 400px, 세로 500px로 확대, 
        resizeSmall() 메서드는 화면 크기를 가로 200px, 세로 250px로 축소하는 기능을 
        가지게 된다. 
    '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

'''
    Big 버튼과 Small 버튼을 눌러서 창의 크기를 확대, 축소할 수 있다.
'''
