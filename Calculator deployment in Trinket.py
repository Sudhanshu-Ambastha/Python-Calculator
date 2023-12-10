choice = input("choose operator...+,-,*,/ or") 
num1 = int(input("enter first number:")) 
num2 = int(input("enter second number:"))

if choice == "+":
   result = num1 + num2
   print("Result:", result)
elif choice == "-":
   result = num1 - num2
   print("Result:", result)
elif choice == "*":
   result = num1 * num2
   print("Result:", result)
elif choice == "/":
   result = num1 / num2
   print("Result:", result)
else:
   print("Invalid choice...")
