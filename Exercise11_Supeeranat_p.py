number = int(input("Please select height of pyramid: "))
for i in range(number):
    print(" "*(number-i)+"*"*(1+2*i)+" "*(number-i))
    i +=1


