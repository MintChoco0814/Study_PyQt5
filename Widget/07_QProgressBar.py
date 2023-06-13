'''
    QProgressBar 위젯은 수평, 수직의 진행 표시줄을 제공.
    setMinimum()과 setMaximum() 메서드로 진행 표시줄의 최솟값과 최대값을 설정할 수 있으며,
    또는 setRange() 메서드로 한 번에 범위를 설정할 수도 있다. 기본값은 0과 99이다.

    setValue() 메서드로 진행 표시줄의 진행 상태를 특정 값으로 설정할 수 있고,
    reset() 메서드는 초기 상태로 되돌린다.

    진행 표시줄의 최소값과 최대값을 모두 0으로 설정하면, 진행 표시줄은 위의 그림과 같이
    항상 진행 중인 상태로 표시된다. 이 기능은 다운로드하고 있는 파일의
    용량을 알 수 없을 때 유용하게 사용할 수 있다.
'''

# ProgressBar.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self) # QProgressBar 생성자로 진행 표시줄을 하나 만들어준다.
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer() # 진행 표시줄을 활성화하기 위해, 타이머 객체를 사용
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step += 1
        self.pbar.setValue(self.step)
    '''
        각각의 QObject와 그 자손들은 timerEvent() 이벤트 핸들러를 갖는다.
        타이머 이벤트에 반응하기 위해, 이벤트 핸들러를 재구성 해준다.
    '''

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self) # 타이머 이벤트를 실행하기 위해, start() 메서드를 호
            self.btn.setText('Stop')
'''
    doAction() 메서드 안에서, 타이머를 시작하고 멈추도록 해준다.
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())