def left (x):
    print (x)

def right (x):
    print("%60s%d"%(" ",x))

odd = False
numberofpage = int(input("Please enter a page number..."))
if (numberofpage %2==0):
    odd = False
    left(numberofpage)
else:
     odd = False
     right(numberofpage)
