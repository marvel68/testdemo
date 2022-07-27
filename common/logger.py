import logging
import os
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Handler(QObject, logging.Handler):
    new_record = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        super(logging.Handler).__init__()

    def emit(self, record):
        """输出格式可以按照自己的意思定义HTML格式"""
        record_dict = record.__dict__

        asctime = record_dict['asctime'] + " >> "
        line = record_dict['filename'] + " -> line:" + str(record_dict['lineno']) + " | "
        levelname = record_dict['levelname']
        message = record_dict['message']

        html = asctime + line + levelname + message
        time.sleep(0.5)

        self.new_record.emit(str(html))  # 将日志信息传给父类 write 函数 需要在父类定义一个函数
        QtWidgets.QApplication.processEvents()

class Logger():

    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')  # 日志输出格式

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()  # 控制台输出

        self.console.setLevel(logging.DEBUG)  # 设置控制台输出级别
        self.filelogger.setLevel(logging.DEBUG)

        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)  # 设置控制台输出格式

        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)  # 控制台输出


    def get_log(self):
        return self.logger


Logger = Logger().logger
# Logger = Logger().get_log()
if __name__ == '__main__':
    Logger.info("---测试开始---")
    Logger.debug("---测试结束---")
