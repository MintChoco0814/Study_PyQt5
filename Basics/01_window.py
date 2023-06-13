import sys
from PyQt5.QtWidgets import QApplication, QWidget
# 필요한 모듈들을 불러온다. 기본적인 UI 구성요소를 제공하는 위젯들은 PyQt5.QtWidgets 모듈에 포함되어 있다.


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') # 타이틀바에 나타나는 창의 제목을 설정한다.
        self.move(300, 300) # 위젯을 스크린의 x,y의 위치로 이동시킨다.
        self.resize(400, 200) # 위젯의 크기를 너비 400px, 높이 200px로 조절한다.
        self.show() # 위젯을 스크린에 보여준다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())