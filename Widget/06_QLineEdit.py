'''
    QLineEdit은 할 줄의 문자열을 입력하고 수정할 수 있도록 하는 위젯이다.

    echoMode()를 설정함으로써 '쓰기 전용' 영역으로 사용할 수 있다.
    이 기능은 비밀번호와 같은 입력을 받을 때 유용하게 사용된다.

    maxLength() 메서드로 입력되는 텍스트의 길이를 제한할 수 있고,
    setValidator() 메서드로 입력되는 텍스트의 종류를 제한할 수도 있다.

    setText() Ehsms insert() 메서드로, 텍스트를 편집할 수 있고, text() 메서드로
    입력된 텍스트를 가져올 수 있다.
    만약 echoMode에 의해 입략되는 텍스트와 표시되는 텍스트가 다르다면,
    displayText() 메서드로 표시되는 텍스트를 가져올 수도 있다.

    setSelection(), selectAll() 메서드로 텍스트로 선택하거나, cut(), copy(), paste()메서드를
    통해 잘라내기, 복사하기, 붙여넣기 등의 동작을 수행할 수 있다.
    또한 setAlignment() 메서드로 텍스트의 정렬을 설정할 수 있다.

    텍스트가 변경되거나 커서가 움직일 때, textChanged(),
    cursorPositionChanged()와 같은 시그널이 발생한다.
'''

# QLineEdit

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qle = QLineEdit(self) # QLineEdit 위젯을 만들었다.
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged) # qle의 텍스트가 바뀌면, onChanged() 메서드를 호출한다.

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
    '''
        onChanged() 메서드 안에서, 입력된 "text"를 라벨 위젯(lbl)의 텍스트로 설정하도록 한다.
        
        또한 adjustSize() 메서드로 텍스트의 길이에 따라 라벨의 길이를 조절해주도록 한다. 
    '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())