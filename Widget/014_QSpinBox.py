#   QSpinBox 클래스는 정수를 선택, 조절하도록 하는 스핀 박스 위젯을 제공한다.

# QSpinBox

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.lbl1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        '''
            QSpinBox 객체 (self.spinbox)를 하나 만든다.
            
            setMinimum()과 setMaximum() 메서드를 이용해서 선택 범위를 제한할 수 있다.
            최소값은 0, 최대값은 99가 디폴트다.
        '''
        # self.spinbox.setRange(-10, 30)
        self.spinbox.setSingleStep(2) # setSingleStep()을 이용해서 한 스텝을 2로 설정한다.
        # 스핀 박스의 경우, 한 스텝으로 설정할 수 있는 최소값은 1이다.
        self.lbl2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.value_changed)
        '''
            스핀 박스 위젯의 값이 변경될 때 발생하는 시그널 (valueChanged)을 
            self.value_changed 메서드에 연결한다.
        '''

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()
        '''
            수직 박스 레이아웃을 이용해서 라벨 두 개와 스핀 박스 위젯을 
            수직으로 배치하고, 전체 위젯의 레이아웃으로 설정한다.
        '''

        self.setLayout(vbox)

        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value()))
    '''
        스핀 박스의 값이 변경될 때, self.lbl2의 텍스트를 스핀 박스의 값(self.spinbox.value())으로 설정하도록 한다.
    '''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())