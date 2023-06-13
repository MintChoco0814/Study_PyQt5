'''
    다이얼 위젯으로 조절한 값을 화면에
    출력하는 프로그램을 만들어 보자

    다이얼의 값이 변할 때 발생하는 시그널이
    LCD 화면에 숫자를 표시하는 슬롯과 연결된다.
'''

# 연결하기
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        '''
            QLCDNumber 위젯은 LCD 화면과 같이 숫자를 표시한다.
            
            QDial은 회전해서 값을 조절하는 위젯이다.
        '''

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)
        '''
            수직 박스 레이아웃을 하나 만들어서 QLCDNumber와 QDial 위젯을 넣어준다.
            
            그리고 MyApp 위젯의 레이아웃으로 설정한다.
        '''

        dial.valueChanged.connect(lcd.display)
        '''
            QDial 위젯은 몇 가지 시그널을 갖고 있다. 
            
            여기서는 valueChanged 시그널을 lcd의 display 슬롯에 연결한다. 
            display 슬롯은 숫자를 받아서
            
            QLCDNumber 위젯에 표시하는 역할을 한다.
            
            여기서 시그널을 보내는 객체인 송신자 (sender)는 dial,
            시그널을 받는 객체인 수신자 (receiver)는 lcd 이다.
            
            슬롯 (slot)은 시그널에 어떻게 반응할지를 구현한 메서드이다.
        '''

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# 다이얼을 움직이면 그 값에 맞춰서 LCD에 숫자가 표시된다.

