import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('../web.png')) # 어플리케이션 아이콘을 설정하도록 합니다.
        # 이를 위해서 QIcon 객체를 생성하였습니다. QIcon()에 보여질 이미지 ('web.png')를 입력합니다.
        self.setGeometry(300, 300, 300, 200) # 창의 위치와 크기를 설정합니다.
        # 앞의 두 매개변수는 창의 x,y 위치를 결정하고, 뒤의 두 매개변수는 각각 창의 너비와 높이를 결정합니다.
        # 이 메서드는 move()와 resize() 메서드를 하나로 합쳐놓은 것과 같습니다.
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
