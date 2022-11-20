from PyQt5.QtWidgets import QMainWindow
from view.ui.ui_AddDateTemplate import Ui_AddDateWidget


class AddDateWindow(QMainWindow):
    def __init__(self):
        super(AddDateWindow, self).__init__()
        self.ui = Ui_AddDateWidget(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass
