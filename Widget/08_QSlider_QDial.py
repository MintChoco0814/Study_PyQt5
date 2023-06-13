'''
    QSlider는 수평 또는 수직 방향의 슬라이더를 제공
    슬라이더는 제한된 범위 안에서 값을 조절하는 위젯

    슬라이더의 틱(tick)의 간격을 조절하기 위해서는 setTickInterval() 메서드, 틱(tick)의
    위치를 조절하기 위해서는 setTickPosition() 메서드를 사용

    setTickInterval() 메서드의 입력값은 픽셀이 아니라 값을 의미.

    QDial은 슬라이더를 둥근 형태로 표현한 다이얼 위젯이며, 기본적으로 같은 시그널과 슬롯,
    메서드들을 공유한다.
'''
# QSlider & QDial

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.slider = QSlider(Qt.Horizontal, self) # QSlider 위젯을 하나 만들었습니다. Qt.Horizontal 또는 Qt.Vertical을 입력해줌으로써 수평 또는 수직 방향을 설정합니다.
        self.slider.move(30, 30)
        #
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)
        '''
            setRange() 메서드로 값의 범위를 0에서 50까지로 설정. setSingleStep() 메서드는 조절 가능하는 최소 단위를 설정.
        '''
        #

        self.dial = QDial(self) # QDial 위젯을 하나 만들었다.
        self.dial.move(30, 50)
        self.dial.setRange(0, 50) # 슬라이더와 마찬가지로 setRange() 메서드로 범위를 정해준다.

        btn = QPushButton('Default', self)
        btn.move(35, 160)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        '''
            슬라이더와 다이얼의 값이 변할 때 발생하는 시그널을 각각 다이얼과 슬라이더의 값을 조절해주는 메서드 (setValue)에 서로 연결함으로 써 두 위젯의 값이
            언제나 일치하도록 해
        '''
        btn.clicked.connect(self.button_clicked) # 'Default' 푸시 버튼을 클릭하면 발생하는 시그널을 button_clicked 메서드에 연

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)

        '''
            button_clicked() 메서드는 슬라이더와 다이얼의 값을 모두 0으로 조절한다.
            따라서 'Default' 푸시 버튼을 클릭하면, 슬라이더와 다이얼의 값이 0으로 초기화된다.
        '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())