from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Booking(QtWidgets.QMainWindow):
    def __init__(self):
        super(Booking,self).__init__()#call the inheritated classes __init__ method
        uic.loadUi("Desing_1.ui",self)#Load the .ui file
        self.setWindowIcon(QtGui.QIcon(r"./images/leasing.png"))
        self.unitUI()
        
    def unitUI(self):
        self.hireCostBtn = self.findChild(QtWidgets.QPushButton,"hireCostBtn")
        self.hireCostBtn.clicked.connect(self.btn_hireCost)
        self.resetBtn.clicked.connect(self.btn_reset)
        self.btnCustomerNew.clicked.connect(self.btnNewCustomer)
        self.btnCustomerExisting.clicked.connect(self.btnExistingCustomer)
        
        
    def btnExistingCustomer(self):
        #set the buttons to be enabled
        self.btnBronzePackage.setEnabled(True)
        self.btnBronzePackage.setAutoExclusive(True)
        self.btnSilverPackage.setEnabled(True)
        self.btnSilverPackage.setAutoExclusive(True)
        self.btnGoldPackage.setEnabled(True)
        self.btnGoldPackage.setAutoExclusive(True)
        
    def btnNewCustomer(self):
        #make the buttons to be unenables
        self.btnBronzePackage.setEnabled(False)
        self.btnSilverPackage.setEnabled(False)
        self.btnGoldPackage.setEnabled(False)
        #make the buttons to not have any values
        self.btnBronzePackage.setAutoExclusive(False)
        self.btnBronzePackage.setChecked(False)
        self.btnBronzePackage.setAutoExclusive(True)
        
        self.btnSilverPackage.setAutoExclusive(False)
        self.btnSilverPackage.setChecked(False)
        self.btnSilverPackage.setAutoExclusive(True)
        
        self.btnGoldPackage.setAutoExclusive(False)
        self.btnGoldPackage.setChecked(False)
        self.btnGoldPackage.setAutoExclusive(True)
       
    def btn_hireCost(self):
        self.validation_checkup()

            
    def validation_checkup(self):
        #btnList = [[self.btnSaloon,22.50],[self.btnHP,28.00],[self.btnVan,35.00]]
        vehicleType = self.check_clicked(self.btnSaloon,self.btnHP,self.btnVan,label=self.vehicleType)
        insuranceCover = self.check_clicked(self.btnInsuranceYes,self.btnInsuranceNo,label=self.insuranceCover)
        typeCustomer = self.check_clicked(self.btnCustomerNew,self.btnCustomerExisting,label=self.customerType)
        if self.btnCustomerExisting.isChecked():
            loyaltyCard = self.check_clicked(self.btnBronzePackage,self.btnSilverPackage,self.btnGoldPackage,label=self.loyaltyCardType)
        
    def check_clicked(self,*args,label=None):
        """Funtion that checks if any of the buttons from the input is checked, if not the label will change its colour in red."""
        arg_list = [*args]
        checked = False
        label.setStyleSheet("color:black;")
        for element in arg_list:
            if element.isChecked():
                checked = True
        if checked == True:
            return True
        else:
            label.setStyleSheet("color:red;")
                
        
    def btn_reset(self):
        #Resets the window to the default values
        self.btnSaloon.setAutoExclusive(False)
        self.btnSaloon.setChecked(False)
        self.btnSaloon.setAutoExclusive(True)
        
        self.btnHP.setAutoExclusive(False)
        self.btnHP.setChecked(False)
        self.btnHP.setAutoExclusive(True)
        
        self.btnVan.setAutoExclusive(False)
        self.btnVan.setChecked(False)
        self.btnVan.setAutoExclusive(True)
        #making the spin box to have the init value to be 1
        self.dayList.setValue(1)
        #seting the radio buttons to the default values
        self.btnInsuranceYes.setAutoExclusive(False)
        self.btnInsuranceYes.setChecked(False)
        self.btnInsuranceYes.setAutoExclusive(True)
        
        self.btnInsuranceNo.setAutoExclusive(False)
        self.btnInsuranceNo.setChecked(False)
        self.btnInsuranceNo.setAutoExclusive(True)
        #setting the customer type to the default values
        self.btnCustomerNew.setAutoExclusive(False)
        self.btnCustomerNew.setChecked(False)
        self.btnCustomerNew.setAutoExclusive(True)
        
        self.btnCustomerExisting.setAutoExclusive(False)
        self.btnCustomerExisting.setChecked(False) 
        self.btnCustomerExisting.setAutoExclusive(True)    
        #setting the loyalty card type to the default values
        self.btnBronzePackage.setEnabled(False)
        self.btnSilverPackage.setEnabled(False)
        self.btnGoldPackage.setEnabled(False)
        
        self.btnBronzePackage.setAutoExclusive(False)
        self.btnBronzePackage.setChecked(False)
        self.btnBronzePackage.setAutoExclusive(True)
        
        self.btnSilverPackage.setAutoExclusive(False)
        self.btnSilverPackage.setChecked(False)
        self.btnSilverPackage.setAutoExclusive(True)
        
        self.btnGoldPackage.setAutoExclusive(False)
        self.btnGoldPackage.setChecked(False)
        self.btnGoldPackage.setAutoExclusive(True)
        #setting the text to the default values
        self.vehicleType.setStyleSheet("color:black")
        self.insuranceCover.setStyleSheet("color:black")
        self.customerType.setStyleSheet("color:black")
        self.loyaltyCardType.setStyleSheet("color:black")
        self.selectLabel.setText("Select")

    

        
        
        
if __name__ == "__main__":      
    app = QtWidgets.QApplication(sys.argv)
    booking = Booking()
    booking.show()
    app.exec_()
