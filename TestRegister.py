from CashRegister import CashRegister

register1 = CashRegister()

user_input = int(input("Please enter the amount of items you have:"))

for i in range (0, user_input):
    a = register1.addItem(int(input("Please enter the cost of one item:" )))

b = register1.giveChange(int(input("Please enter your payment:" )))

print("Total price is: ", register1._totalPrice)
print("There are ", register1._itemCount, "items.")
print("Change is: ", register1._change)
