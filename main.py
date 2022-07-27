import logging
import multiprocessing
import sys
import run

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from Ui_Dialog import Ui_Dialog
from common.logger import Handler, Logger
from common.LiteLog import LiteLog
from threads import ResThread

class Window(QWidget, Ui_Dialog):
    def __init__(self):
        super(Window, self).__init__()
        self.thread = None
        self.setupUi(self)

        self.handler = Handler()
        multiprocessing.get_logger().addHandler(self.handler)
        Logger.addHandler(self.handler)
        Logger.setLevel(logging.DEBUG)
        self.Logger=LiteLog(name=__name__)
        self.Logger.bindQTlog(self.textBrowser)
        self.test_start.clicked.connect(self.buttonClick)
    def buttonClick(self):
        self.textBrowser.clear()
        self.runner=run.runner(self.Logger)
        self.thread = ResThread(target=self.runner.run)
        self.thread.start()

if __name__ == "__main__":
    import cgitb
    cgitb.enable(format='text')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())