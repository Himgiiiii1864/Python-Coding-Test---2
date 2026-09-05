def add(x, y):
  return x + y
  
def subtract(x, y):
  return x - y
  
def multiply(x, y):
  return x * y
  
def divide(x, y):
  return x / y

operation = input("Enter the operation you would like to carry out(ADD, SUBTRACT, MULTIPLY, DIVIDE): ").strip().upper()

try:
  num1 = float(input("Enter your first number: "))
except ValueError:
  print("Invalid Input. Enter a valid number.")

try:
  num2 = float(input("Enter your second number: "))
except ValueError:
  print("Invalid Input. Enter a valid number.")

if operation == "ADD":
  print("The answer is: ", add(num1, num2))
elif operation == "SUBTRACT":
  print("The answer is: ", subtract(num1, num2))
elif operation == "MULTIPLY":
  print("The answer is: ", multiply(num1, num2))
elif operation == "DIVIDE":
  try:
    print("The answer is: ", divide(num1, num2))
  except ZeroDivisionError:
    print("Division by zero is not defined. Enter a valid number.")
else:
  print("Kindly select a valid operation.")