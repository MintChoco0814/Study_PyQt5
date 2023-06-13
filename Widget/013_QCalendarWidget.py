'''
    QCalendarWidget을 이용해서 사용자가 날짜를 선택할 수 있도록 달력을
    포시할 수 있다.

    달력은 월 단위로 표시되고, 처음 실행될 때 현재의 연도, 월, 날짜로 선택되어 있다.
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        '''
            QCalenderWidget의 객체(cal)를 하나 만든다.
            setGridVisible(True)로 설정하면, 날짜 사이에 그리드가 표시 
            날짜를 클릭했을 때 showDate 메서드가 호출되도록 연결해준다.
        '''

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        '''
            selectedDate는 현재 선택된 날짜 정보를 갖고 있다. (디폴트는 현재 날짜) 
            현재 날짜 정보를 라벨을 표시되도록 해준다.
        '''

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        '''
            수직 박스 레이아웃을 이용해서, 
            달력과 라벨을 수직으로 배치해준다.
        '''

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()
    def showDate(self, date):
        self.lbl.setText(date.toString())
        '''
            showDate 메서드에서, 
            날짜를 클릭할 때마다 라벨 텍스트가 선택한 날짜(date.toString())로 표시되도록 한다.
        '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())