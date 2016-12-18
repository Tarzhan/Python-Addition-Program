def f(a) :
    if a < 0:
        return -1
    n = a
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            return n
        elif n == 1:
            return 1
        else:
            n = 3 * n + 1
    return 0

a = [-1, 0, 1, 2, 10, 100]

def main():
    
    for i in a:
        print("Results for f(",i, ") is: )", f(i))

main()
