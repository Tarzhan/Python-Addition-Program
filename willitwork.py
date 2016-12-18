from CashRegister import CashRegister

class testregister(CashRegister):
   CashRegister.itemCount = 0
   CashRegister.totalPrice = 0
   CashRegister.additional = 0

   
                          
     while CashRegister.change < 0:
       print("You still have to pay ", round(CashRegister.chanage*-1,2))
       CashRegister.additional = float(input("How much more are you paying? "))
       CashRegister.change = CashRegister.change + round(CashRegister.additional,2)

     else:
          print("Your change is ", round(CashRegister.change,2))

     return(CashRegister.change)


register1 = testregister()
register1.addItem(20)
register1.addItem(14)


print("The number of items is ",register1.getCount())
print("The total price is ", register1.totalPrice)
money = float(input("Enter Amount "))

register1.givechange(money)
