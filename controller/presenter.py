
from PyQt5.QtWidgets import QTableWidgetItem

from model.model import Model

import random


class Presenter:
    ''' it is glue between view and model '''
    is_add = False
    is_edit = False 
    
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.init_view()        
        self.current_view = None
        #objects
        self.companies = []
        self.canalizations = []
         
    def init_view(self):
        ''' set all view buttons and action True '''
        
        # home init
        self.view.home_view.ui.CompaniesPushButton.clicked.connect(self.goto_company)
        self.view.home_view.ui.CanalizationsPushButton.clicked.connect(self.goto_canalization)
        self.view.home_view.ui.PollutantsPushButton.clicked.connect(self.goto_pollutant)
        self.view.home_view.ui.ExitHomePushButton.clicked.connect(self.exit_session)
        # company init
        self.view.company_view.ui.AddCompanyPushButton.clicked.connect(self.goto_add_company)
        self.view.company_view.ui.EditCompanyPushButton.clicked.connect(self.goto_edit_company)
        self.view.company_view.ui.DeleteCompanyPushButton.clicked.connect(self.goto_delete_company)
        self.view.company_view.ui.CompanyBackPushButton.clicked.connect(self.back_home)
        self.view.company_view.ui.ShowCompanyPushButton.clicked.connect(self.show_company)
        # canalization init
        self.view.canalization_view.ui.AddCanalizationPushButton.clicked.connect(self.goto_add_canalization)
        self.view.canalization_view.ui.EditCanalizationPushButton.clicked.connect(self.goto_edit_canalization)
        self.view.canalization_view.ui.DeleteCanalizationPushButton.clicked.connect(self.goto_delete_canalization)
        self.view.canalization_view.ui.CanalizationBackPushButton.clicked.connect(self.back_home)
        self.view.canalization_view.ui.ShowCanalizationPushButton.clicked.connect(self.show_canalization)    
        # add/edit company init
        self.view.add_edit_company_view.ui.AddEditCompanyBackPushButton.clicked.connect(self.back_home)
        self.view.add_edit_company_view.ui.CompanyConfirmPushButton.clicked.connect(self.confirm_company)
        self.view.add_edit_company_view.ui.WaterUseTypeComboBox.addItems(Model.WATER_USE_TYPES)
        # add/edit canalization init
        self.view.add_edit_canalization_view.ui.ADdEditcanalizationBackPushButton.clicked.connect(self.back_home)
        self.view.add_edit_canalization_view.ui.CanalizationConfirmPushButton.clicked.connect(self.confirm_canalization)
        # pollutant init
        self.view.pollutant_view.ui.PollutantAddDatePushButton.clicked.connect(self.goto_add_date)
        self.view.pollutant_view.ui.PollutantBackPushButton.clicked.connect(self.back_home) 
        self.view.pollutant_view.ui.ShowPollutantPushButton.clicked.connect(self.show_task_five)
        self.view.pollutant_view.ui.AddPollutantPushButton.clicked.connect(self.goto_add_pollutant)    
        # add pollutant init
        self.view.add_pollutant_view.ui.PollutantConfirmPushButton.clicked.connect(self.confirm_pollutant)
        self.view.add_pollutant_view.ui.AddPollutantBackPushButton.clicked.connect(self.back_home) 
        self.view.add_pollutant_view.ui.PollutantGroupComboBox.addItems(Model.POLLUTANT_GROUPS)
        self.view.add_pollutant_view.ui.PollutantDangerClassComboBox.addItems(Model.POLLUTANT_DANGER_CLASSES)
        # add date init
        self.view.add_date_view.ui.DateConfirmPushButton.clicked.connect(self.confirm_date)
        self.view.add_date_view.ui.AddDateBackPushButton.clicked.connect(self.back_home) 
        

    def back_home(self):
        self.view.widgets.setCurrentWidget(self.view.home_view)
    
    #COMPANY    
    def goto_company(self):
        self.current_view = self.view.company_view
        self.view.widgets.setCurrentWidget(self.current_view)
        
        if not self.companies:
            self.companies = self.model.get_company_name()
            for company in self.companies:
                self.current_view.ui.SelectCompanyComboBox.addItem(company[0])
    
    def show_company(self):
        selected_name = self.current_view.ui.SelectCompanyComboBox.currentText()
        data = self.model.get_company_detail(name=selected_name)
        text = f"""<p><b>Name:</b> {data[0]}</p><p><b>Water use type:</b> {data[1]}</p>"""
        self.current_view.ui.CompanyInfoTextBrowser.setText(text)

    def goto_add_company(self):
        Presenter.is_edit = False
        Presenter.is_add = True
        
        self.current_view = self.view.add_edit_company_view
        self.view.widgets.setCurrentWidget(self.current_view)
    
    def goto_edit_company(self):
        Presenter.is_edit = True
        Presenter.is_add = False 
        
        self.current_view = self.view.add_edit_company_view
        self.view.widgets.setCurrentWidget(self.current_view)
    
    def confirm_company(self):
        context = {
                "name": self.current_view.ui.CompanyNameLineEdit.text(),
                "water_use_type": self.current_view.ui.WaterUseTypeComboBox.currentText()
            }
        if Presenter.is_edit:
            old_name = self.view.company_view.ui.SelectCompanyComboBox.currentText()
            context["old_name"] = old_name
            updated_name = self.model.update_company(context)
            index = self.view.company_view.ui.SelectCompanyComboBox.findText(old_name)
            
            self.view.company_view.ui.SelectCompanyComboBox.removeItem(index)
            self.view.company_view.ui.SelectCompanyComboBox.addItem(updated_name)
            self.companies.remove((old_name,))
            self.companies.append((updated_name,))
            
            self.view.company_view.ui.CompanyInfoTextBrowser.setText("")
        elif Presenter.is_add:
            new_name = self.model.add_company(context)
            
            self.view.company_view.ui.SelectCompanyComboBox.addItem(new_name)
            self.companies.append((new_name,))
        self.goto_company()
        
    def goto_delete_company(self):
        selected_name = self.current_view.ui.SelectCompanyComboBox.currentText()
        if self.model.delete_company(selected_name):
            self.companies.remove((selected_name,))
            index = self.current_view.ui.SelectCompanyComboBox.findText(selected_name)
            self.current_view.ui.SelectCompanyComboBox.removeItem(index)
            self.current_view.ui.CompanyInfoTextBrowser.setText("")
        
    # CANALIZATION    
    def goto_canalization(self):
        self.current_view = self.view.canalization_view
        self.view.widgets.setCurrentWidget(self.current_view)
        
        if not self.canalizations:
            self.canalizations = self.model.get_canalization_name()
            for canalization in self.canalizations:
                self.current_view.ui.SelectCanalizationComboBox.addItem(canalization[0])
    
    def show_canalization(self):
        selected_name = self.current_view.ui.SelectCanalizationComboBox.currentText()
        data = self.model.get_canalization_detail(name=selected_name)
        text = f"""<p><b>Name:</b> {data[0]}</p>
                    <p><b>Company:</b> {data[1]}</p>
                    <p><b>Control Gate:</b> {data[2]}</p>
                    <p><b>Height:</b> {data[3]}</p>
                    <p><b>Shore Distance:</b> {data[4]}</p>
                    <p><b>Control Gate Distance:</b> {data[5]}</p>
                    <p><b>Water Waste:</b> {data[6]}</p>
                    <p><b>Angle:</b> {data[7]}</p>
                    <p><b>Min Water Speed:</b> {data[8]}</p>
                    <p><b>Hole Diameter:</b> {data[9]}</p>"""
        self.current_view.ui.CanalizationInfoTextBrowser.setText(text)
    
    def goto_add_canalization(self):
        Presenter.is_edit = False
        Presenter.is_add = True
        
        self.current_view = self.view.add_edit_canalization_view
        self.fill_company_combobox()
        self.fill_control_gate_combobox()
        self.view.widgets.setCurrentWidget(self.current_view)
    
    def fill_company_combobox(self):
        self.current_view.ui.CanalizationCompanyComboBox.clear()
        for item in self.model.get_company_name():
            self.current_view.ui.CanalizationCompanyComboBox.addItem(item[0])    
            
    def fill_control_gate_combobox(self):
        self.current_view.ui.CanalizationControlGateComboBox.clear()
        for item in self.model.get_control_gate_name():
            self.current_view.ui.CanalizationControlGateComboBox.addItem(item[0])    
        
    def goto_edit_canalization(self):
        Presenter.is_edit = True
        Presenter.is_add = False 
        
        self.current_view = self.view.add_edit_canalization_view
        self.fill_company_combobox()
        self.fill_control_gate_combobox()
        self.view.widgets.setCurrentWidget(self.current_view)
    
    def confirm_canalization(self):
        context = {
                "name": self.current_view.ui.CanalizationNameLineEdit.text(),
                "company": self.current_view.ui.CanalizationCompanyComboBox.currentText(),
                "control_gate": self.current_view.ui.CanalizationControlGateComboBox.currentText(),
                "shore_distance": self.current_view.ui.CanalizationShoreDIstanceSpinBox.value(),
                "control_gate_distance": self.current_view.ui.CanalizationControlGateDistanceSpinBox.value(),
                "height": self.current_view.ui.CanalizationHeightDoubleSpinBox.value(),
                "angle": self.current_view.ui.CanalizationAngleSpinBox.value(),
                "min_water_speed": self.current_view.ui.CanalizationMinWaterSpeedDoubleSpinBox.value(),
                "water_waste": self.current_view.ui.CanalizationWaterWasteDoubleSpinBox.value(),
                "hole_diameter": self.current_view.ui.CanalizationHoleDiameterDoubleSpinBox.value(),
            }
        if Presenter.is_edit:
            old_name = self.view.canalization_view.ui.SelectCanalizationComboBox.currentText()
            context["old_name"] = old_name
            updated_name = self.model.update_canalization(context)
            index = self.view.canalization_view.ui.SelectCanalizationComboBox.findText(old_name)
            
            self.view.canalization_view.ui.SelectCanalizationComboBox.removeItem(index)
            self.view.canalization_view.ui.SelectCanalizationComboBox.addItem(updated_name)
            self.canalizations.remove((old_name,))
            self.canalizations.append((updated_name,))
            
            self.view.canalization_view.ui.CanalizationInfoTextBrowser.setText("")
        elif Presenter.is_add:
            new_name = self.model.add_canalization(context)
            self.view.canalization_view.ui.SelectCanalizationComboBox.addItem(new_name)
            self.canalizations.append((new_name,))
        self.goto_canalization()
        
    def goto_delete_canalization(self):
        selected_name = self.current_view.ui.SelectCanalizationComboBox.currentText()
        if self.model.delete_canalization(selected_name):
            self.canalizations.remove((selected_name,))
            index = self.current_view.ui.SelectCanalizationComboBox.findText(selected_name)
            self.current_view.ui.SelectCanalizationComboBox.removeItem(index)
            self.current_view.ui.CanalizationInfoTextBrowser.setText("") 
       
    # POLLUTANT 
    def goto_add_date(self):
        Presenter.is_edit = False
        Presenter.is_add = True
        
        self.current_view = self.view.add_date_view
        self.view.widgets.setCurrentWidget(self.current_view)
        self.fill_pollutant_combobox()
        
    def fill_pollutant_combobox(self):
        self.current_view.ui.DatePollutantComboBox.clear()
        for item in self.model.get_pollutant_name():
            self.current_view.ui.DatePollutantComboBox.addItem(item[0])
        
    def show_task_five(self):
        table = self.view.pollutant_view.ui.TaskFiveTableWidget
        table.setRowCount(0)
        company = self.view.pollutant_view.ui.PollutantCompanyComboBox.currentText()
        date = self.current_view.ui.PollutantDateComboBox.currentText()
        
        data_list = self.model.get_task_five_data(company, date)
        for data in data_list:
            row = table.rowCount()
            table.setRowCount(row+1)
            col = 0
            for item in data:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col += 1 
    
    def show_task_three(self):
        table = self.view.pollutant_view.ui.TaskThreeTableWidget
        table.setRowCount(0)
        data_list = self.model.get_task_three_data()
        for data in data_list:
            row = table.rowCount()
            table.setRowCount(row+1)
            col = 0
            for item in data:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col += 1
                
    def show_task_four(self):
        table = self.view.pollutant_view.ui.TaskFourTableWidget
        table.setRowCount(0)
        data_list = self.model.get_task_four_data()
        for data in data_list:
            row = table.rowCount()
            table.setRowCount(row+1)
            col = 0
            for item in data:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col += 1
    
    def refresh_all_tasks(self):
        self.show_task_three()
        self.show_task_four()
        
    
    def goto_pollutant(self):
        self.current_view = self.view.pollutant_view
        self.view.widgets.setCurrentWidget(self.current_view)
        
        self.refresh_all_tasks()
        
        self.current_view.ui.PollutantCompanyComboBox.clear()
        for item in self.model.get_company_name():
            self.current_view.ui.PollutantCompanyComboBox.addItem(item[0])
        self.fill_date_combobox()
    
    def fill_date_combobox(self):
        self.view.pollutant_view.ui.PollutantDateComboBox.clear()
        for item in self.model.get_dates():
            self.view.pollutant_view.ui.PollutantDateComboBox.addItem(item[0])
    
    def goto_add_pollutant(self):
        Presenter.is_edit = False
        Presenter.is_add = True
        
        self.current_view = self.view.add_pollutant_view
        self.view.widgets.setCurrentWidget(self.current_view)
        self.fill_canalization_combobox()
        
        
    def fill_canalization_combobox(self):
        self.current_view.ui.PollutantCanalizationComboBox.clear()
        for item in self.model.get_canalization_name():
            self.current_view.ui.PollutantCanalizationComboBox.addItem(item[0])
    
    def confirm_pollutant(self):
        context = {
            "name": self.current_view.ui.PollutantNameLineEdit.text(),
            "canalization": self.current_view.ui.PollutantCanalizationComboBox.currentText(),
            "group": self.current_view.ui.PollutantGroupComboBox.currentText(),
            "danger_class": self.current_view.ui.PollutantDangerClassComboBox.currentText(),
            "knk": self.current_view.ui.PollutantKNKSpinBox.value(),
            "lfv": self.current_view.ui.PollutantLFVSpinBox.value(),
            "pds": random.randint(100, 500)
        }
        
        if Presenter.is_add:
            name = self.model.add_pollutant(context)
            self.refresh_all_tasks()            
            
        self.goto_pollutant()
    
    def confirm_date(self):
        context = {
            "date": str(self.current_view.ui.DateEdit.date().toPyDate()),
            "pollutant": self.current_view.ui.DatePollutantComboBox.currentText(),
            "control_gate_bc": self.current_view.ui.DateControlGateBCSpinBox.value(),
            "canalization_bc": self.current_view.ui.DateCanalizationBCSpinBox.value(),
            "pdk": self.current_view.ui.DatePDKSpinBox.value()
        }
        
        if Presenter.is_add:
            date = self.model.add_date(context)
            self.fill_date_combobox()
            
        self.goto_pollutant()

    @staticmethod
    def exit_session():
        exit()
    