from CashRegister import CashRegister

r1 = Cashregister()       #default cash register
r2 = Cashregister(1,0.7)  #cashregister with custom values

print(r1.getCount())
print("test ",r2.getTotal())
print("test ",r2.getCount())
print("test ",r2.addItem())
