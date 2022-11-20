from PyQt5.QtWidgets import QMainWindow
from view.ui.ui_PollutantTemplate import Ui_PollutanWidget


class PollutantWindow(QMainWindow):
    def __init__(self):
        super(PollutantWindow, self).__init__()
        self.ui = Ui_PollutanWidget(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass
