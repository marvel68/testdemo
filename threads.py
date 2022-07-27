from PyQt5.QtCore import QThread

from run import run


class Example(QThread):

    def __init__(self):
        super(Example, self).__init__()



    def run(self):
        """
        进行任务操作，主要的逻辑操作,返回结果
        """
        run()
