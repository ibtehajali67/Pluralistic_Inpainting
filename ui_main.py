import os
import sys
from options.test_options import TestOptions
os.environ['QT_QPA_PLATFORM']='offscreen'
from gui.ui_model import ui_model
from PyQt5 import QtWidgets


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    opt = TestOptions().parse()
    #print()
    my_gui = ui_model(opt)
    my_gui.show()
    sys.exit(app.exec_())
