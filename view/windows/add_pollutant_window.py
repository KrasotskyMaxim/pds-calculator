from PyQt5.QtWidgets import QMainWindow
from view.ui.ui_AddPollutantTemplate import Ui_AddPollutantWidget


class AddPollutantWindow(QMainWindow):
    def __init__(self):
        super(AddPollutantWindow, self).__init__()
        self.ui = Ui_AddPollutantWidget(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass
