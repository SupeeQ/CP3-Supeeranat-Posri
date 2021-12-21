Menulist = []
def CreateMenu():
    while True:
        Addmenu = input("Please enter your menu name: ")
        if Addmenu.lower() == "exit":
            break
        else:
            AddPrice = int(input("Please enter your menu price: "))
            Menulist.append([Addmenu,AddPrice])
def Showmenu():
    Total = 0
    for number in range(len(Menulist)):
        print(Menulist[number])
        Total = Total + Menulist[number][1]
    print("Total sum is:", Total)
CreateMenu()
Showmenu()

