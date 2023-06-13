'''
    메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의
    레이아웃을 갖고 있습니다.

    또한 가운데 영역에 중심위젯 (Central widget)을 위한 영역을 갖고 있습니다.
    여기에는 어떠한 위젯도 들어올 수 있씁니다.

    QMainWindow 클래스를 이용해서 메인 어플리케이션 창을 만들 수 있습니다.
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.statusBar().showMessage('Ready') # 상태바에 보여질 메세지를 설정할 수 있다.

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())