# 이번에는 mouseMoveEvent를 이용해서 마우스의 위치를 트래킹해서 출력해보자.
# 이벤트 핸들러 재구성 2

import sys
from typing import Union

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 0
        y = 0

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(20, 20)
        '''
            x, y의 값을 self.text로 저장하고, self.label의 텍스트로 설정
            
            위치를 x = 20, y = 20 만큼 이동해준다.
        '''

        self.setMouseTracking(True)
        '''
            setMouseTracking을 True로 설정해주면, 마우스의 위치를 트래킹한다.
            
            디폴트는 setMouserTracking(False) 상태이며, 
            마우스 버튼을 클릭하거나 뗄 때만 mouseEvent가 발생한다.
        '''

        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mouserMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x {0}, y: {1}".format(x, y)
        self.label.setText(text)
        self.label.adjustSize()
    '''
        이벤트 e는 이벤트에 대한 정보를 갖고 있는 하나의 객체이다.
        이 이벤트 객체는 생성된 이벤트의 유형에 따라 다르다.
        
        e.x(), e.y()는 위젯 안에서 이벤트가 발생했을 때 마우스 커서의 위치를 반환한다.
        
        만약 e.globalX(), e.globalY()로 설정해주면, 화면 전체에서 마우스 커서의 위치를 반환하게 된다.
        
        self.label.adjustSize() 메서드로 라벨의 크기를 자동으로 조절하도록 한다.
    '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# 위젯 안에서 마우스를 움직이면 이벤트가 발생, 재구성한 이벤트 핸들러를 통해 마우스의 위치를 출력
