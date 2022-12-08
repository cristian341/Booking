def calculationPrice():
    costs = {"Saloon":22.50,"High Performance":28.00,"Van":35.00}
    car = "Saloon" #self.btnVehicle.text()
    days = 4 #self.dayList.value()
    insurance = "Yes" #self.btnInsurance.text()
    customer = "New" #self.btnCustomer.text()
    #loyalty = self.gettingLoyalty()
    cover = 0
    if insurance == "Yes":
        cover = 15.50
    print(float(costs[car])*days+cover)

calculationPrice()
        