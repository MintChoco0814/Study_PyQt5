# QDateTimeEdit 위젯은 사용자에게 날짜와 시간을 선택, 편집하도록 할 때 사용한다.
# QDateTimeEdit

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateTimeEdit, QVBoxLayout
from PyQt5.QtCore import QDateTime

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QTimeEdit')

        datetimeedit = QDateTimeEdit(self)
        datetimeedit.setDateTime(QDateTime(QDateTime.currentDateTime()))
        datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        '''
            QDateTimeEdit 클래스를 이용해서 날짜, 시간 편집 위젯(datetimeedit)을 하나 만들어준다.
            
            setDateTime 메서드에 QDateTime.currentDateTime()을 입력해서 프로그램이 실행될 때 
            현재 날짜와 시간으로 표시되도록 한다.
            
            setDateTimeRange를 이용하면 사용자가 선택할
        '''
        datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')
        '''
            setDisplayFormat 메서드를 이용해서 시간이 'yyyy.MM.dd hh:mm:ss'의 형식으로
            표시되도록 설정함
        '''

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(datetimeedit)
        vbox.addStretch()
        '''
            수직 박스 레이아웃을 이용해서 라벨과 날짜, 시간 편집 위젯을 수직으로 배치, 
            전체 위젯의 레이아웃으로 설정한다.
        '''
        self.setLayout(vbox)

        self.setWindowTitle('QDateTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
