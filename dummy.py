def transication():
    pass

def planning():
    pass

def expenses():
    pass


print("Welcome to Personal Finance Management System")
print(" 1.Transication \n 2.Planning \n 3.Expenses \n 4.Exit the program")
respond = int(input("Your Choice: "))
while True:
    if respond == 1:
        transication()
    elif respond == 2:
        planning()
    elif respond == 3:
        expenses()
    elif respond == 4:
        break
print("Thank You")