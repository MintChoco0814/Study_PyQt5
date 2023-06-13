'''
    QMessageBox 클래스는 사용자에게 정보를 제공하거나 질문과 대답을 할 수 있는 대화창 제공

    흔히 어떤 동작에 대해 확인이 필요한 경우에 메세지 박스를 사용함.

    메세지 박스에서는 사용자에게 상황을 설명하는 기본 텍스트를 표시한다.
    그 다음 정보를 전달하거나 사용자의 의사를 묻는 텍스트를 표시할 수 있다.

    마지막으로 더욱 자세히 상황을 설명하기 위한 세부적인 텍스트를 표시할 수 있다.
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class MyApp(QWidget):
    '''
        QWidget을 종룔할 때, QCloseEvent가 생성되어 위젯에 전달된다.
        위젯의 동작을 수정하기 위해 closeEvent() 이벤트 핸들러를 수정해야 한다.
    '''
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300 ,300, 200)
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        '''
            두 번째 매개변수는 타이틀바에 나타날 문자열 ('Message'), 세번째 매개변수는
            대화창에 나타날 문자열 ('Are you sure to quit?')을 입력 
            
            네 번째에는 대화창에 보여질 버튼의 종류를 입력하고, 
            마지막으로 디폴트로 선택될 버튼을 설정해준다.
            
            QMessageBox.No로 설정할 경우, 메세지 박스가 나타났을 때 'No'버튼이 선택되어 있다.
            반환 값은 reply 변수에 저장된다.
        
        '''
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        '''
            'Yes' 버튼을 클릭했을 경우, 이벤트를 받아들이고 위젯을 종료한다.
            
            'No' 버튼을 클릭하면, 이벤트를 무시하고 위젯을 종료하지 않는다.
        '''

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# 이제 창을 닫을 때, 이 동작을 한 번 더 확인하기 위한 메세지 박스가 나타나게 된다.