def calc_this(number, op):
    if(op == "+"):
        number+=number
    elif(op == "-"):
        number -= 4
    elif(op == "x"):
        number*=number
    elif(op == "/"):
        number /= number
    else:print("Invalid input")

    print("Your number is, ", number)


print("Welcome to the calculator")
num = int(input("Enter a number that you would like to perform an opeartion on: "))
operation = str(input("Enter the operation you want performed addition(+), subtration(-), multiplication(x), or division(/): "))

calc_this(num, operation)
