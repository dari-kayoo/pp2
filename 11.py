what = input("what you need? (+, -, *, /)")
a = float(input("first number:"))
b = float(input("second number:"))
if what == "+":
        c = a + b
        print("REsult:" + str(c)  )
elif what == "-":
        c = a - b
        print("REsult:" + str(c))  
elif what == "*":
        c = a*b
        print("REsult:" + str(c))  
else:
        print("Problem")