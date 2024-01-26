
def add_num(num1, num2):
  return num1 + num2
  
def sub_num(num1, num2):
  return num1 - num2

def mul_num(num1, num2):
  return num1 * num2

def div_num(num1, num2):
  return num1 / num2


input1 = int(input("Enter a number ")) 
input2 = int(input("Enter a number "))
userInput = input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide ")


if userInput == "1":
  print("The answer is " + str(add_num(input1, input2)))
elif userInput == "2":
  print("The answer is " + str(sub_num(input1, input2)))
elif userInput == "3":
  print("The answer is " + str(mul_num(input1, input2)))
elif userInput == "4":
  print("The answer is " + str(div_num(input1, input2)))

else:
  print("Invalid choice")
