from PyQt5.QtWidgets import QMainWindow
from view.ui.ui_HomeTemplate import Ui_HomeWidget


class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.ui = Ui_HomeWidget(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass
