# ------------------------------Inputs---------------------

# name = input("Name : ")
# age = input("Age : ")
# print("hey" , name)

# --------------------------------Calc---------------------
# radius = input("Enter the redius (m) : ")
# area = 3.142*int(radius)**2
# print("the area of the circle is", area)


# --------------------------------Formating----------------
# n1 = 1.23456789
# n2 = 50.6549873
# print("n1 is {:.3f} and n2 is {:.3}".format(n1,n2))

#using F-STRINGS
# print(f'n1 is {n1:.3f} and n2 is {n2:.3}')


# --------------------------------IF-Statement----------------
# age = int(input("Your age : "))
# if (age >= 19 and age !=25):
#     print("your age is higher that 19")
# elif age <10 and age!= 25:
#     print("Your age is lower than 10")
# elif age == 25:
#     print("Your age is 25")
# else :
#     print("Your age is else")


# --------------------------------For-Loops-------------------
# listt = ['yacine','mitchell','rain']
# for element in listt[1:3]:
#         print(element,"\n")


# for element in listt:
#     if (element =='mitchell'):
#         print(f"Nickname is {element}")
#         break
#     else :
#         print (f"Not nickname {element}")

# ------------------------------While-Loops-------------------
age = 25
num = 0

while num < age :
    if (num==0):
        num=1
        continue
    if (num%2==0):
        print (num)
    num+=1