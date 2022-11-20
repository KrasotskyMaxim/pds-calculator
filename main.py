# XDG_SESSION_TYPE=x11

# pyqt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QStackedWidget

#MVP
from view.windows.home_window import HomeWindow
from view.windows.company_window import CompanyWindow
from view.windows.canalization_window import CanalizationWindow
from view.windows.pollutant_window import PollutantWindow
from view.windows.add_edit_company_window import AddEditCompanyWindow
from view.windows.add_edit_canalization_window import AddEditCanalizationWindow
from view.windows.add_pollutant_window import AddPollutantWindow
from view.windows.add_date_window import AddDateWindow

from controller.presenter import Presenter
from model.model import Model

# system
import sys


class App(QApplication):
    def __init__(self, *args):
        super().__init__(list(args))
        
        # view
        self.widgets = QStackedWidget()
        self.home_view = HomeWindow()
        self.company_view = CompanyWindow()
        self.canalization_view = CanalizationWindow()
        self.pollutant_view = PollutantWindow()
        self.add_edit_company_view = AddEditCompanyWindow()
        self.add_edit_canalization_view = AddEditCanalizationWindow()
        self.add_pollutant_view = AddPollutantWindow()
        self.add_date_view = AddDateWindow()
        
        #model
        self.model = Model()
        
        # presenter
        self.presenter = Presenter(view=self, model=self.model)
        
        self.init_app()
        
    def init_app(self):
        # add widgets
        self.widgets.addWidget(self.home_view)
        self.widgets.addWidget(self.company_view)
        self.widgets.addWidget(self.canalization_view)
        self.widgets.addWidget(self.pollutant_view)
        self.widgets.addWidget(self.add_edit_company_view)
        self.widgets.addWidget(self.add_edit_canalization_view)
        self.widgets.addWidget(self.add_pollutant_view)
        self.widgets.addWidget(self.add_date_view)
        # sizes
        self.widgets.setFixedHeight(800)
        self.widgets.setFixedWidth(600)
        # show
        self.widgets.setCurrentWidget(self.home_view)
        self.widgets.show()


def application():
    app = App(sys.argv)
    app.setApplicationName("PDS calculator")
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    application()