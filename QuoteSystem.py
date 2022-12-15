from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Quote(QtWidgets.QMainWindow):
    def __init__(self):
        super(Quote,self).__init__()#call the inheritated classes __init__ method
        uic.loadUi("Design.ui",self)#Load the .ui file
        self.setWindowIcon(QtGui.QIcon(r"./images/leasing.png"))
        self.unitUI()
        
    def unitUI(self):
        """Getting the event driven object"""
        self.Header.setCurrentWidget(self.QuoteCalculator)   
        self.hiddenVariables()     
        self.hireCostBtn.clicked.connect(self.btn_hireCost)
        self.resetBtn.clicked.connect(self.btn_reset)
        self.btnCustomersReset.clicked.connect(self.btn_reset)
        self.btnCustomerNew.clicked.connect(self.btnNewCustomer)
        self.btnCustomerExisting.clicked.connect(self.btnExistingCustomer)
        
    def hiddenVariables(self):
        """Setting the hidden variables"""
        self._costs = {"Saloon":22.50,"High Performance":28.00,"Van":35.00}
        self._cover = 15.50
        self._discount = 0.9
        self._returnable = 50
        self._promotionDiscount = 18.00
        
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
        """Quote Calculation main funtion"""
        #If the validation is true, when it will precide with the quote calculation and quote displaying by calling textPrint()
        if self.validation_checkup():
            self.Header.setCurrentWidget(self.QuoteViewer)
            
            self.textPrint()
            discount, totalCost = self.calculationPrice()
            self.totalPriceLabel.setText(f"Total Price is £{totalCost:.2f}")
            self.totalPriceLabel.adjustSize()
            
            self.discountLabel.setText(f"{discount*100}%")
            self.discountLabel.adjustSize()
            
            self.returnableLabel.setText(f"£{self._returnable}")
            self.returnableLabel.adjustSize()
            
            self.depositLabel.setText(f"£{self._returnable}")
            self.depositLabel.adjustSize()
            
            
    def validation_checkup(self):
        """Its getting the button's label, which has been clicked"""
        "Checkes if the required buttons had been pressed, to"
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
        """Sets all the buttons/labals to default values."""
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
        self.pricePerLabel.setText("£0.00")
        self.daysLabel.setText("")
        self.insuranceTypeLabel.setText("")
        self.customerTypeLabel.setText("")
        self.loyaltyTypeCard.setText("")
        self.discountLabel.setText("0%")
        self.returnableLabel.setText("£0.00")
        self.returnableLabel.adjustSize()
        self.depositLabel.setText("£0.00")
        self.depositLabel.adjustSize()
        self.totalPriceLabel.setText("Total Price is £0.00")
        
        self.Header.setCurrentWidget(self.QuoteCalculator)
        
        
    def textPrint(self):
        """Prints that button's text, that has been chose"""
        self.carTypeLabel.setText(self.btnVehicle.text())
        self.carTypeLabel.adjustSize()
        
        self.pricePerLabel.setText(f"£{self._costs[self.btnVehicle.text()]:.2f}")
        self.pricePerLabel.adjustSize()
        
        self.daysLabel.setText(f"{self.dayList.value()}")
        self.daysLabel.adjustSize()
         
        self.insuranceTypeLabel.setText(self.btnInsurance.text())
        self.insuranceTypeLabel.adjustSize()
        
        self.customerTypeLabel.setText(self.btnCustomer.text())
        self.customerTypeLabel.adjustSize()
        
        self.loyaltyTypeCard.setText(self.gettingLoyalty())
        self.loyaltyTypeCard.adjustSize()
        
    def gettingLoyalty(self):
        """Its getting the loyalty card type only if the customer is an existing customer, otherwise it will display none."""
        if self.btnCustomerExisting.isChecked():
            return self.btnPackage.text()
        else:
            return "None"
        
    def calculationPrice(self):
        
        if self.dayList.value() >= 7 and self.btnInsurance.text() == "Yes" and self.gettingLoyalty() == "Gold":
            if self.btnVehicle.text() == "Saloon":
                totalCost = ((self._costs[self.btnVehicle.text()] * self.dayList.value()) + self._cover) * self._discount + self._returnable
                print(1)
                return 0.1, totalCost
            elif self.btnVehicle.text() == "High Performance":
                totalCost = ((self._costs[self.btnVehicle.text()] * self.dayList.value()) + self._cover - self._promotionDiscount) * self._discount + self._returnable
                print(2)
                return 0.1, totalCost
            elif self.btnVehicle.text() == "Van":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() + self._cover) * self._discount + self._returnable
                print(3)
                return 0.1, totalCost
            
        elif self.dayList.value() >= 7 and self.btnInsurance.text() == "Yes":
            if self.btnVehicle.text() == "Saloon":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() + self._cover) * self._discount + self._returnable
                print(4)
                return 0.1, totalCost
            elif self.btnVehicle.text() == "High Performance":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() + self._cover) * self._discount + self._returnable
                print(5)
                return 0.1, totalCost
            elif self.btnVehicle.text() == "Van":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() + self._cover) * self._discount + self._returnable
                print(6)
                return 0.1, totalCost
            
        elif self.dayList.value() >= 7 and self.gettingLoyalty() == "Gold":
            if self.btnVehicle.text() == "Saloon":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) * self._discount + self._returnable
                print(7)
                return 0.1, totalCost
            elif self.btnVehicle.text() == "High Performance":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() - self._promotionDiscount) * self._discount + self._returnable
                print(8)
                return 0.1, totalCost
            elif self.btnVehicle.text() == "Van":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) * self._discount + self._returnable
                print(9)
                return 0.1, totalCost
            
        elif self.btnInsurance.text() == "Yes" and self.gettingLoyalty() == "Gold":
            if self.btnVehicle.text() == "Saloon":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() + self._cover) + self._returnable
                print(10)
                return 0, totalCost
            elif self.btnVehicle.text() == "High Performance":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() + self._cover - self._promotionDiscount) + self._returnable
                print(11)
                return 0, totalCost
            elif self.btnVehicle.text() == "Van":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) + self._cover + self._returnable
                print(12)
                return 0, totalCost
            
        elif self.dayList.value() >= 7:
            if self.btnVehicle.text() == "Saloon":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) * self._discount + self._returnable
                print(13)
                return 0.1, totalCost
            elif self.btnVehicle.text() == "High Performance":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) * self._discount + self._returnable
                print(14)
                return 0.1, totalCost
            elif self.btnVehicle.text() == "Van":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) * self._discount + self._returnable
                print(15)
                return 0.1, totalCost
            
        elif self.btnInsurance.text() == "Yes":
            if self.btnVehicle.text() == "Saloon":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() + self._cover) + self._returnable
                print(16)
                return 0, totalCost
            elif self.btnVehicle.text() == "High Performance":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() + self._cover) + self._returnable
                print(17)
                return 0, totalCost
            elif self.btnVehicle.text() == "Van":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() + self._cover) + self._returnable 
                print(18)
                return 0, totalCost
            
        elif self.gettingLoyalty() == "Gold":
            if self.btnVehicle.text() == "Saloon":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) + self._returnable
                print(19)
                return 0, totalCost
            elif self.btnVehicle.text() == "High Performance":
                
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value() - self._promotionDiscount) + self._returnable
                print(19)
                return 0, totalCost
            elif self.btnVehicle.text() == "Van":
                
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) + self._returnable
                print(20)
                return 0, totalCost
        
        elif self.btnInsurance.text() == "No":
            if self.btnVehicle.text() == "Saloon":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) + self._returnable
                print(21)
                return 0, totalCost
            elif self.btnVehicle.text() == "High Performance":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) + self._returnable
                print(22)
                return 0, totalCost
            elif self.btnVehicle.text() == "Van":
                totalCost = (self._costs[self.btnVehicle.text()] * self.dayList.value()) + self._returnable
                print(23)
                return 0, totalCost
            
        
        
if __name__ == "__main__":      
    app = QtWidgets.QApplication(sys.argv)
    quote = Quote()
    quote.show()
    app.exec_()
 