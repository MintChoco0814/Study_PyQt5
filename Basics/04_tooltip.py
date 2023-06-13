import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):

     def __init__(self):
        super().__init__()
        self.initUI()
     def initUI(self):
         QToolTip.setFont(QFont('SansSerif', 10)) # 10px 크기의 'SansSerif' 폰트를 사용
         self.setToolTip('This is a <b>QWidget</b> widget') # 표시될 텍스트를 입력해 준다.

         btn = QPushButton('Button', self) # 푸시버튼을 만든다.
         btn.setToolTip('This is a <b>QPushButton</b> widget') # 이 버튼에도 툴팁을 달아준다.
         btn.move(50, 50) # 버튼의 위치와 크기
         btn.resize(btn.sizeHint()) # sizeHint() 메서드느느 적절한 크기로 설정하도록 도와줍니다.

         self.setWindowTitle('Tooltips')
         self.setGeometry(300, 300, 300, 200)
         self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())