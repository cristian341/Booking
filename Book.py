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
        self.costs = {"Saloon":22.50,"High Performance":28.00,"Van":35.00}
        
    def unitUI(self):
        self.Header.setCurrentWidget(self.Hire)
        self.comboBoxHP.setPlaceholderText("Text")
        self.hireCostBtn.clicked.connect(self.btn_hireCost)
        self.resetBtn.clicked.connect(self.btn_reset)
        self.btnCustomersReset.clicked.connect(self.btn_reset)
        self.btnCustomerNew.clicked.connect(self.btnNewCustomer)
        self.btnCustomerExisting.clicked.connect(self.btnExistingCustomer)
        
        
    def btnExistingCustomer(self):
        "set the buttons to be enabled"
        self.btnBronzePackage.setEnabled(True)
        self.btnBronzePackage.setAutoExclusive(True)
        self.btnSilverPackage.setEnabled(True)
        self.btnSilverPackage.setAutoExclusive(True)
        self.btnGoldPackage.setEnabled(True)
        self.btnGoldPackage.setAutoExclusive(True)
        
    def btnNewCustomer(self):
        "make the buttons to be unenables"
        self.btnBronzePackage.setEnabled(False)
        self.btnSilverPackage.setEnabled(False)
        self.btnGoldPackage.setEnabled(False)
        "make the buttons to not have any values"
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
        """Geting the information which button was pressed"""
        if self.validation_checkup():
            self.Header.setCurrentWidget(self.Customers)
            """Start the quote preparation"""
            self.textPrint()
            discount, returnable, totalCost = self.calculationPrice()
            self.totalPriceLabel.setText(f"Total Price is £{totalCost:.2f}")
            self.totalPriceLabel.adjustSize()
            
            self.discountLabel.setText(f"{discount*100}%")
            self.discountLabel.adjustSize()
            
            self.returnableLabel.setText(f"£{returnable}")
            self.returnableLabel.adjustSize()
            
            
    def validation_checkup(self):
        "geting the if the buttons are pressed"
        self.btnVehicle = self.check_clicked(self.btnSaloon,self.btnHP,self.btnVan,label=self.vehicleType)
        self.btnInsurance = self.check_clicked(self.btnInsuranceYes,self.btnInsuranceNo,label=self.insuranceCover)
        self.btnCustomer = self.check_clicked(self.btnCustomerNew,self.btnCustomerExisting,label=self.customerType)
        if self.btnCustomerExisting.isChecked():
            self.btnPackage = self.check_clicked(self.btnBronzePackage,self.btnSilverPackage,self.btnGoldPackage,label=self.loyaltyCardType)
            if self.btnVehicle and self.btnInsurance and self.btnCustomer and self.btnPackage:
                return True
        elif self.btnCustomerNew.isChecked():
            if self.btnVehicle and self.btnInsurance and self.btnCustomer:
                return True
            
       
    def check_clicked(self,*args,label=None):
        """Funtion that checks if any of the buttons from the input is checked, if not the label will change its colour in red."""
        arg_list = [*args]
        label.setStyleSheet("color:black;")     
        for element in arg_list:
            if element.isChecked():
                return element
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

        self.carTypeLabel.setText("")
        self.priceLabel.setText("£0.00")
        self.daysLabel.setText("")
        self.insuranceTypeLabel.setText("")
        self.customerTypeLabel.setText("")
        self.loyaltyTypeCard.setText("")
        self.discountLabel.setText("0%")
        self.returnableLabel.setText("£0.00")
        self.returnableLabel.adjustSize()
        self.totalPriceLabel.setText("Total Price is £0.00")
        
        
    def textPrint(self):
        
        self.carTypeLabel.setText(self.btnVehicle.text())
        self.carTypeLabel.adjustSize()
        
        #self.carModelLabel.setText(self.)
        #self.carModelLabel.adjustSize()
        
        self.daysLabel.setText(f"{self.dayList.value()}")
        self.daysLabel.adjustSize()
         
        self.insuranceTypeLabel.setText(self.btnInsurance.text())
        self.insuranceTypeLabel.adjustSize()
        
        self.customerTypeLabel.setText(self.btnCustomer.text())
        self.customerTypeLabel.adjustSize()
        
        self.loyaltyTypeCard.setText(self.gettingLoyalty())
        self.loyaltyTypeCard.adjustSize()
        
    def gettingLoyalty(self):
        if self.btnCustomerExisting.isChecked():
            return self.btnPackage.text()
        else:
            return "None"
        
    def calculationPrice(self):
        self.costs = {"Saloon":22.50,"High Performance":28.00,"Van":35.00}
        cover = 0.00
        discount = 0.00
        returnable = 50
        promotionDiscount = 0.00 
        
        if self.dayList.value() >= 7 and self.btnInsurance.text() == "Yes" and self.gettingLoyalty() == "Gold":
            if self.btnVehicle.text() == "Saloon":
                discount = 0.9
                cover = 15.50
                totalCost = ((self.costs[self.btnVehicle.text()] * self.dayList.value()) + cover + returnable) * discount
                print(1)
                return 0.1, returnable, totalCost
            elif self.btnVehicle.text() == "High Performance":
                discount = 0.9
                cover = 15.50
                promotionDiscount = 18.00
                totalCost = ((self.costs[self.btnVehicle.text()] * self.dayList.value()) + cover + returnable - promotionDiscount) * discount
                print(2)
                return 0.1, returnable, totalCost
            elif self.btnVehicle.text() == "Van":
                discount = 0.9
                cover = 15.50
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable) * discount
                print(3)
                return 0.1, returnable, totalCost
            
        elif self.dayList.value() >= 7 and self.btnInsurance.text() == "Yes":
            if self.btnVehicle.text() == "Saloon":
                discount = 0.9
                cover = 15.50
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable) * discount
                print(4)
                return 0.1, returnable, totalCost
            elif self.btnVehicle.text() == "High Performance":
                discount = 0.9
                cover = 15.50
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable) * discount
                print(5)
                return 0.1, returnable, totalCost
            elif self.btnVehicle.text() == "Van":
                discount = 0.9
                cover = 15.50
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable) * discount
                print(6)
                return 0.1, returnable, totalCost
            
        elif self.dayList.value() >= 7 and self.gettingLoyalty() == "Gold":
            if self.btnVehicle.text() == "Saloon":
                discount = 0.9
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + returnable) * discount
                print(7)
                return 0.1, returnable, totalCost
            elif self.btnVehicle.text() == "High Performance":
                discount = 0.9
                promotionDiscount = 18.00
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() - promotionDiscount+ returnable) * discount
                print(8)
                return 0.1, returnable, totalCost
            elif self.btnVehicle.text() == "Van":
                discount = 0.9
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + returnable) * discount
                print(9)
                return 0.1, returnable, totalCost
            
        elif self.btnInsurance.text() == "Yes" and self.gettingLoyalty() == "Gold":
            if self.btnVehicle.text() == "Saloon":
                cover = 15.50
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable) 
                print(10)
                return discount, returnable, totalCost
            elif self.btnVehicle.text() == "High Performance":
                cover = 15.50
                promotionDiscount = 18.00
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover - promotionDiscount + returnable)
                print(11)
                return discount, returnable, totalCost
            elif self.btnVehicle.text() == "Van":
                discount = 0.9
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + returnable)
                print(12)
                return discount, returnable, totalCost
            
        elif self.dayList.value() >= 7:
            if self.btnVehicle.text() == "Saloon":
                discount = 0.9
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + returnable) * discount
                print(13)
                return 0.1, returnable, totalCost
            elif self.btnVehicle.text() == "High Performance":
                discount = 0.9
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + returnable) * discount
                print(14)
                return 0.1, returnable, totalCost
            elif self.btnVehicle.text() == "Van":
                discount = 0.9
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + returnable) * discount
                print(15)
                return 0.1, returnable, totalCost
            
        elif self.btnInsurance.text() == "Yes":
            if self.btnVehicle.text() == "Saloon":
                cover = 15.50
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable)
                print(16)
                return discount, returnable, totalCost
            elif self.btnVehicle.text() == "High Performance":
                cover = 15.50
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable)
                print(17)
                return discount, returnable, totalCost
            elif self.btnVehicle.text() == "Van":
                cover = 15.50
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable) 
                print(18)
                return discount, returnable, totalCost
            
        elif self.gettingLoyalty() == "Gold":
            if self.btnVehicle.text() == "Saloon":
                promotionDiscount = 18.00
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover - promotionDiscount + returnable)
                print(19)
                return discount, returnable, totalCost
            elif self.btnVehicle.text() == "High Performance":
                promotionDiscount = 18.00
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover - promotionDiscount + returnable)
                print(19)
                return discount, returnable, totalCost
            elif self.btnVehicle.text() == "Van":
                promotionDiscount = 18.00
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover - promotionDiscount + returnable)
                print(20)
                return discount, returnable, totalCost
        
        elif self.btnInsurance.text() == "No":
            if self.btnVehicle.text() == "Saloon":
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable)
                print(21)
                return discount, returnable, totalCost
            elif self.btnVehicle.text() == "High Performance":
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable)
                print(22)
                return discount, returnable, totalCost
            elif self.btnVehicle.text() == "Van":
                totalCost = (self.costs[self.btnVehicle.text()] * self.dayList.value() + cover + returnable)
                print(23)
                return discount, returnable, totalCost
            
        
        
if __name__ == "__main__":      
    app = QtWidgets.QApplication(sys.argv)
    booking = Booking()
    booking.show()
    app.exec_()
 