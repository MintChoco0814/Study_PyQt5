"""
    그룹 박스는 상단 타이틀과 단축기 (shortcut)를 제공하며, 그 안에 다양한 위젯들을 나타낼 수 있다.

    QGroupBox 클래스는 제목과 제목의 정렬을 설정하도록 해준다.
    그룹 박스는 체크 가능하도록 설정할 수 있는데, 그룹 박스의 체크 여부에 따라 그 그룹 박스 안에 있는 위젯들이 사용 가능하거나 불가능해진다.

    공간을 절약하기 위해 flat 속성을 활성화할 수 있는데, 보톤 프레임의 왼쪽, 오른쪽, 아래쪽 가장자리가 없게 표시된다.
"""

# QGroupBox

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)
        '''
            그리드 레이아웃을 이용해서 그룹박스를 배치합니다. 
            각 메서드를 통해 만들어지는 그룹박스가 addWidget()을 통해 각 위치로 배치됩니다.
        '''
        self.setLayout(grid)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox
    '''
        createFirstExclusiveGroup() 메서드는 배타적인 라디오버튼을 갖는 그룹박스를 만듭니다.
        
        메서드는 먼저 그룹박스 (groupbox)를 만들고, 버튼을 만든 다음 수직 박스 레이아웃을 통해 배치한다.
        
        마지막으로 수직 박스 레이아웃 (vbox)를 그룹 박스의 레이아웃으로 설정한다.
        
        세 개의 라디오버튼을 만들고 수직으로 배치했다.
    '''

    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')
        groupbox.setChecked(True)
        groupbox.setChecked(False)

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        checkbox = QCheckBox('Independent Checkbox')
        checkbox.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True)
        '''
            createNonExclusiveGroup() 메서드는 배타적이지 않은 체크박스들을 갖는 그룹박스를 만든다.
            
            setFlat()을 이용해서 그룹박스를 평평하게 보이도록 한다.
        '''

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox


    def createPushButtonGroup(self):
        groupbox = QGroupBox('Push Button')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)
        '''
            createPushButtonGroup() 메서드는 여러 개의 푸시버튼을 갖는 그룹 박스를 만든다.
            
            setCheckable()과 setChecked()를 이용해서, 그룹 박스를 선택 가능하게, 
            그리고 실행했을 때 선택되어 있도록 설정한다.
        '''
        pushbutton = QPushButton('Normal Button')
        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True)
        popupbutton = QPushButton('Popup Button')
        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())