'''
    QRadioButton 위젯은 사용자가 선택할 수 있는 버튼을 만들 때 사용한다. 이 버튼에도 체크 박스와 마찬가지로 텍스트 라벨이 하나 포함된다.

    라디오 버튼은 일반적으로 사용자에게 여러 개 중 하나의 옵션을 선택하도록 할 떄 사용된다.
    그래서 한 위젯 안에 여러 라디오 버튼은 기본적으로 autoExclusive로 설정되어 있다.

    하나의 버튼을 선택하면 나머지 버튼들은 선택 해제가 된다.

    한 번에 여러 버튼을 선택할 수 있도록 하려면 setAutoExclusive() 메서드에 False를 입력해주면 된다.
    또한 한 위젯 안에 여러 개의 exclusive 버튼 그룹을 배치하고 싶다면 QButtonGroup() 메서드를 사용할 수 있다.

    체크 박스와 마찬가지로 버튼의 상태가 바뀔 때, toggled() 시그널이 발생한다. 또한 특정 버튼의 상태를 가져오고 싶을 때,
    isChecked() 메서드를 사용할 수 있다.
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        rbtn1 = QRadioButton('First Button', self) # QRadioButton을 하나 만듭니다. 라벨에 들어갈 텍스트와 부모 위젯을 입력한다.
        rbtn1.move(50, 50)
        rbtn1.setChecked(True) # setChecked()를 True로 설정하면 프로그램이 실행될 때 버튼이 선택되어 표시된다.

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button') # setText() 메서드를 통해서도 라벨의 텍스트를 설정할 수 있다.

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())