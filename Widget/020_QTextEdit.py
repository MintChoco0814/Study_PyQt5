'''
    QTextEdit 클래스는 플레인 텍스트(plain text)와 리티 텍스트(rich text)를 모두 편집하고 표시할 수 있는
    편집기를 제공
'''

# QTextEdit

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel('The number of words is 0')
        '''
            QTextEdit() 클래스를 이용해서 텍스트 편집기 하나를 만들었습니다.
            
            setAcceptRichText를 False로 하면, 모두 플레인 텍스트로 인식한다.
            아래의 라벨은 단어수를 표시.
        '''
        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)
        '''
            수직 박스 레이아웃을 이용해서,
            두 개의 라벨과 하나의 텍스트 편집기를 수직 방향으로 배치한다.
        '''
        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))
        '''
            text_changed 메서드가 호출되면, toPlainText() 메서드를 이용해서 텍스트 편집기
            (self.te)에 있던 텍스트를 text 변수에 저장한다.
            
            split()은 문자열의 단어들을 리스트 형태로 바꿔준다.
            
            len(text.split())은 text의 단어수이다.
            
            setText()를 이용해서 두 번째 라벨에 단어수를 표시한다.
        '''




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())