'''
    QTextBrowser 클래스는 하이퍼텍스트 내비게이션을 포함하는 리치 텍스트 (서식있는 텍스트) 브라우저를 제공한다.

    이 클래스는 읽기 전용이며, QTextEdit의 확장형으로서 하이퍼텍스트 문서의 링크들을 사용할 수 있다.

    편집 가능한 리치 텍스트 편집기를 사용하기 위해서는 QTextEdit을 사용해야 한다.

    또한 하이퍼텍스트 네비게이션이 없는 텍스트 브라우저를 시용하기 위해서는 QTextEdit을 setReadOnly()를
    사용해서 편집이 불가능하도록 해준다.

    짧은 리치 텍스트를 표시하기 위해서는 QLabel을 사용할 수 있다.
'''

# QTextBrowser

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)
        '''
            줄편집기를 하나를 만들었다.
            Enter키를 누르면 append_text 메서드가 호출된다.
        '''

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        '''
            QTextBrowser() 클래스를 이용해서 텍스트 브라우저를 하나 만들었다.
            setAcceptRichText()를 True로 설정해주면, 서식 있는 텍스트(Rich text)를 사용할 수 있다.
            디폴트로 True이기 때문에 없어도 되는 부분이다.
            setOpenExternalLinks()를 True로 설정해주면, 외부링크로의 연결이 가능하다.
        '''
        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)
        # clear_btn을 클릭하면, clear_text 메서드가 호출된다.
        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()
    '''
        append_text 메서드는 즐편집기에 작성된 텍스트 (self.le.text())를 텍스트 브라우서 (self.tb)에 append 해주는
        기능을 한다.
        
        텍스트가 텍스트 브라우저에 추가되면, clear 메서드를 이용해서 줄편집기에 있던 텍스트는 없애준다.
    
    '''
    def clear_text(self):
        self.tb.clear()
    '''
        clear_text 메서드가 호출되면,
        clear 메서드를 이용해서 텍스트 브라우저 (self.tb)에 있던 텍스트를 없애 준다.
    '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

'''
    Plain Text
    <b>Bold</b> 
    <i>Italic</i> 
    <p style="color:red">Red</p> 
    <p style="font-size: 20px">20px</p> 
    <a href="https://www.naver.com">Naver</a>
'''