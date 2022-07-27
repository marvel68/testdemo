import logging
import multiprocessing
import os
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from Ui_Dialog import Ui_Dialog
from common.logger import Handler, Logger
from threads import Example

class Window(QWidget, Ui_Dialog):
    def __init__(self):
        super(Window, self).__init__()
        self.thread = None
        self.setupUi(self)

        self.handler = Handler()
        multiprocessing.get_logger().addHandler(self.handler)
        Logger.addHandler(self.handler)
        Logger.setLevel(logging.DEBUG)

        self.test_start.clicked.connect(self.buttonClick)
        self.handler.new_record.connect(self.write)

    def write(self, s):
        self.textBrowser.append(s)
        time.sleep(0.5)
        QtWidgets.QApplication.processEvents()

    def buttonClick(self):

        self.textBrowser.clear()
        self.thread = Example()

        self.thread.start()
