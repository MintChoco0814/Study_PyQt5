## 툴바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('../exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction(QIcon('../save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save application')

        printAction = QAction(QIcon('../print.png'), 'Print', self)
        printAction.setShortcut('Ctrl+P')
        printAction.setStatusTip('Print application')

        editAction = QAction(QIcon('../edit.png'), 'Edit', self)
        editAction.setShortcut('Ctrl+E')
        editAction.setStatusTip('Edit application')
        self.statusBar()

        self.toolExitbar = self.addToolBar('Exit')
        self.toolExitbar.addAction(exitAction)

        self.toolSavebar = self.addToolBar('Save')
        self.toolSavebar.addAction(saveAction)

        self.toolPrintbar = self.addToolBar('Print')
        self.toolPrintbar.addAction(printAction)

        self.toolEditbar = self.addToolBar('Edit')
        self.toolEditbar.addAction(editAction)


        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
