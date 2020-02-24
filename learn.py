print("***************wlcome to Ashwani icecream***********")
a = int(input("enter the quantity of orange cream : "))
a = a*5
f = int(input("enter the quantity of fruitbar : "))
f = f*5
m = int(input("enter the quantity of minicup : "))
m = m*5
l = int(input("enter the quantity of largecup : "))
l = l*10
ch = int(input("enter the quantity of chocolate : "))
ch = ch*10
k = int(input("enter the quantity of Kulfi : "))
k = k*10
mk = int(input("enter the quantity of matka kulfi : "))
mk = mk*15
c = int(input("enter the quantity of cone : "))
c = c*20
total = a+f+m+l+ch+k+mk+c
print("Total amount of icecreams",total)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("enter the quantities for return")
a = int(input("enter the quantity of orange cream : "))
a = a*5
f = int(input("enter the quantity of fruitbar : "))
f = f*5
m = int(input("enter the quantity of minicup : "))
m = m*5
l = int(input("enter the quantity of largecup : "))
l = l*10
ch = int(input("enter the quantity of chocolate : "))
ch = ch*10
k = int(input("enter the quantity of Kulfi : "))
k = k*10
mk = int(input("enter the quantity of matka kulfi : "))
mk = mk*15
c = int(input("enter the quantity of cone : "))
c = c*20
tr = a+f+m+l+ch+k+mk+c
print("Total amount of return icecream",tr)
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
sa = total - tr
print("total ammount of selled icecream",sa)
p = (sa*30)/100
print("saved money by hocker",p)
py = sa-p
print("Total amount to be pay is  : ",py)
print("---------------------------------------THANK YOU----------------------")
