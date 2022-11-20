from PyQt5.QtWidgets import QMainWindow
from view.ui.ui_AddEditCompanyTemplate import Ui_AddEditCompanyWidget


class AddEditCompanyWindow(QMainWindow):
    def __init__(self):
        super(AddEditCompanyWindow, self).__init__()
        self.ui = Ui_AddEditCompanyWidget(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass
