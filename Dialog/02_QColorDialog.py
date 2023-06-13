# 컬러 다이얼로그는 색상을 선택할 수 있는 다이얼로그이다.
# QColorDialog

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        col = QColor(0, 0, 0)
        # QColor를 사용해서 배경색인 검정색을 만들었다.

        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background - color : %s }' % col.name())

        self.frm.setGeometry(130, 35, 100, 100)

        self.setWindowTitle('Color Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()
    def showDialog(self):
        col = QColorDialog.getColor()
        '''
            QColorDialog 클래스의 getColor() 메서드는 컬러 다이얼로그 창을 띄우고 사용자가 
            색상을 선택하도록 한다.
            
            그리고 선택한 색상을 QColor 클래스의 형태로 반환한다.
        '''

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background - color: %s}' % col.name())
        '''
            색상을 선택하고 'OK' 버튼을 눌렀다면, col.isValid()의 불 값이 True이고, 'Cancel' 버튼을 눌렀다면,
            불 값이 False가 된다.
            
            선택한 색상이 프레임의 배경색으로 설정된다.
        '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

'''
    우선 푸시 버튼 하나와 QFrame 하나를 만들고, QFrame 위젯의 배경색은 검정색으로 설정했다.
    QColorDialog를 사용해서, 배경색을 바꿀 수 있다.
'''