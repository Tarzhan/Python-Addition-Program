n = 20

def mystery(n):
    if n <= 0:
        return 0
    else:
        return mystery(n//2)+1
     
mystery(n)
print (mystery(n))
