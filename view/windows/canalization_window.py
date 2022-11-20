from PyQt5.QtWidgets import QMainWindow
from view.ui.ui_CanalizationsTemplate import Ui_CompaniesForm


class CanalizationWindow(QMainWindow):
    def __init__(self):
        super(CanalizationWindow, self).__init__()
        self.ui = Ui_CompaniesForm(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass
