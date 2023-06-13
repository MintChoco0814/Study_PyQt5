'''
    푸시 버튼 또는 명령 버튼은 사용자가 프로그램에 명령을 내려서 어떤 동작을 하도록
    할 때 사용되는 버튼이며, GUI 프로그래밍에서 가장 흔하게 사용되고 중요한 위젯이다.
'''

# QPushButton

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()
        ''' 
            QPushButton 클래스로 푸시 버튼을 하나 만듭니다. 첫 번째 파라미터로는 버튼에 
            나타날 텍스트, 두 번째는 버튼이 속할 부모 클래스를 지정해줍니다.
            
            버튼에 단축기(shortcut)를 지정하고 싶으면 아래와 같이 해당 문자 앞에 ampersand('&')를
            넣어주면 돈다. 이 버튼의 단축기는 'Alt+b'가 된다.
            
            setCheckable()을 True로 설정해주면, 선택되거나 선택되지 않은 상태를 유지할 수 있게 된다.
            
            toggle() 메서드를 호출하면 버튼의 상태가 바뀌게 된다. 따라서 이 버튼은 프로그램이 시작될 때 
            선택되어 있다.
        '''

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        '''
            setText() 메서드로도 버튼에 표시될 텍스트를 지정할 수 있다. 
            
            또한 이 버튼의 단축기는 'Alt+2'가 된다.
        '''

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)
        '''
            setEnabled()를 False로 설정하면, 버튼을 사용할 수 없게 된다.
        '''
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())