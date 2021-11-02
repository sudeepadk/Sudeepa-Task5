#Task5
x = int(input("Enter First number : "))
y = int(input("Enter Second number : "))

r = input("Which operation you want to perform? '+,-,*,/,^  :  " )
#'a' for addition, 'b' for subtraction, 'c' for multiplication, 'd' for division, e for squares"
if r == '+':
    a=x+y
    print("Sum =" + str(a) )
elif r== '-':
    b = x - y
    print("Difference = " + str(b))
elif r == '*':
    c = x*y
    print("product = " + str(c))
elif r == '/':
    d = x/y
    print("quotient = " + str(d))
elif r == '^':
    e = x^y
    print("exponent number = " + str(e))
else:
    print("choose from above operators only")



