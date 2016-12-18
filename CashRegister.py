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
       return self._itemCount
    

   def giveChange(self, payment) :
       self._payment=int(payment)
       self.change = self.payment - self.totalPrice
       return (self.change)
       

   def clear(self) :
       self._itemCount = 0
       self._totalPrice = 0.0
 



