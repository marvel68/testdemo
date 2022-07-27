import sys

from Dialog import Window
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import cgitb
    cgitb.enable(format='text')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    # ui = Ui_Dialog()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())