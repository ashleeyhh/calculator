print("Select an operation")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE") 
op = input()
if op=="1":
    num1= input("Enter first number")
    num2= input("Enter second number")
    print("Sum is " +str(int(num1)+int(num2)))
elif op=="2":
    num1= input("Enter first number")
    num2= input("Enter second number")
    print("Difference is " +str(int(num1)-int(num2)))
elif op=="3":
    num1= input("Enter first number")
    num2= input("Enter second number")
    print("Product is " +str(int(num1)*int(num2)))
elif op=="4": 
    num1= input("Enter first number")
    num2= input("Enter second number")
    print(" Remainder is " +str(int(num1)/int(num2)))
else:
    print("Invalid operation") 