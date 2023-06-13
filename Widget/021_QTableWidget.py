'''
    QTableWidget 클래스는 테이블 형태로 항목을 배치하고 다루도록 한다.
'''
# QTableWidget.

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        '''
            QTableWidget 클래스를 사용해서 테이블 위젯을 하나 만들었음
            setRowCount() 메서드는 테이블의 행(Row)의 개수를 지정함.
            setColmnCount() 메서드는 테이블의 열 (Column)의 개수를 지정
        '''

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        '''
            setEditTriggers() 메서드는 테이블의 항목을 편집 가능하도록 하는 액션을 지정함.
            
            QAbstractItemView.NoEditTriggers으로 지정하면 편집을 할 수 없음.
            
            QAbstractItemView.DoubleClicked으로 지정하면 칸을 더블클릭 했을 때 편집이 가능함. 
            
            QAbstractItemView.AllEditTriggers으로 지정하면 클릭, 더블클릭 등 모든 액션에 대해 편집이 
            가능함.
        '''

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidge.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        '''
            horizontalHeader() 는 수평 헤더를 반환한다.
            
            setSectionResizeMode() 메서드는 헤더의 크기를 조절하는 방식을 지정한다.
            
            QHeaderView.Stretch는 헤더의 폭이 위젯의 폭에 맞춰지도록 한다.
            
            QHeaderView.ResizeToContents는 헤더의 폭이 항목 값의 폭에 맞춰지도록 한다.            
        '''

        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(i+j)))

        '''
            setItem(row, column, value) 메서드는 테이블 항목의 값을 지정한다.
            
            순서대로 행과 열의 번호, 그리고 값을 입력.
        
        '''
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
# 20개의 행과 4개의 열을 갖는 테이블 위젯이 만들어진다.