import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication # QtCore 모듈의 QCoreApplication 클래스를 불러옵니다.

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self) # 푸시버튼을 하나 만듭니다.
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit) # 버튼을 클릭하면 'cliked' 시그널이 만들어집니다.
        # clicked 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됩니다.
        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())