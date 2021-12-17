username = input("Please enter your username : ")
password = input("Please enter your password : ")
if username == "abb" and password == "1111":
    print("----Welcome to my shop----")
    print("1.pen              : 10 bath ")
    print("2.eraser           :  5 bath ")
    print("3.ruler            : 20 bath ")
    print("4.coffee           : 17 bath ")
    print("5.Coke             : 12 bath ")
    print("--------------------------")
    order = int(input("Select the item number you would like to buy : "))
    number = int(input("How many item you would like to buy? : "))
    if order == 1:
        print("Pen :", number, "Units")
        print("Total price :", number*10, "bath")
        print("Thank you for your purchase")
    elif order == 2:
        print("eraser :", number, "Units")
        print("Total price :", number*5, "bath")
        print("Thank you for your purchase")
    elif order == 3:
        print("ruler :", number, "Units")
        print("Total price :", number * 20, "bath")
        print("Thank you for your purchase")
    elif order == 4:
        print("coffee :", number, "Units")
        print("Total price :", number * 17, "bath")
        print("Thank you for your purchase")
    elif order == 5:
        print("coke :", number, "Units")
        print("Total price :", number * 20, "bath")
        print("Thank you for your purchase")
    else:
        print("Error")
        print("please select the item again")
else:
    print("Error username or password is incorrect")
    print("Please try again")
