class CashRegister :
   
   def __init__(self) :
       self._itemCount = 0
       self._totalPrice = 0.0
      
   
   def addItem(self, price) :
       self._itemCount = self._itemCount + 1
       self._totalPrice = self._totalPrice + price 
      
   
   def getTotal(self) :
       return self._totalPrice

   def getCount(self) :
       return self._getCount
       

   def clear(self) :
       self._getCount = 0
       self._totalPrice = 0.0

class TestRegister(CashRegister):
   CashRegister.itemCount = 0
   CashRegister.totalPrice = 0
   CashRegister.additional = 0

   def giveChange(self, payment) :
      self.change = 0
      self.payment = float(payment)
      self.change = (self.payment - self._totalprice)
      print("You have given ", round(self.payment,2))

      while self.change < 0:
         print("You still owe ", round(self.change*-1,2))
         self.additional = float(input("How much more would you like to pay? "))
         self.change = self.change + round(self.additional,2)

      else:
         print("Your chanage is ", round(self.change,2))

      return(self.change)

register1 = TestRegister()
register1.addItem(10)
register1.addItem(14)

print("The number of items is ",register1.getCount)
print("The total price is ", register1.totalPrice)
money = float(input("Please enter amount.."))
register1.giveChange(money)
      
      

