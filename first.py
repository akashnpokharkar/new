a= int(input("Enter your first number: "))
b= int(input("Enter your second number: "))


choice= input("what operation you want to do: (choices are +,-,*,%): ")
print(type(choice))

if choice == 'Addition':
    c= a+b
    print("Addition of two numbers is: ", c)

elif choice == 'subtraction':
    c= a-b
    print("Subtrastion of two numbers is: ", c)
else:
    print("Invalid choice")    