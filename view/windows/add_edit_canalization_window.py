from PyQt5.QtWidgets import QMainWindow
from view.ui.ui_AddEditCanalizationTemplate import Ui_AddEditCanalizationWidget

class AddEditCanalizationWindow(QMainWindow):
    def __init__(self):
        super(AddEditCanalizationWindow, self).__init__()
        self.ui = Ui_AddEditCanalizationWidget(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()
                
    def hide_interface(self):
        pass
