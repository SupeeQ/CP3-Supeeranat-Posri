Menulist = []
Menuprice = []

def CreateMenu():
    while True:
        Addmenu = input("Please enter your menu name: ")
        if Addmenu.lower() == "exit":
            break
        else:
            AddPrice = int(input("Please enter your menu price: "))
            Menulist.append(Addmenu)
            Menuprice.append(AddPrice)
def Showmenu():
    Price = 0
    for number in range(len(Menuprice)):
        print(Menulist[number], Menuprice[number])
        Price = Price + float(Menuprice[number])
    return Price

CreateMenu()
print(Showmenu())

