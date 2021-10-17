# ----------------------------- Ranges -----------------------

# for i in range(3,10,2):
#     print(i)

# names = ['mitchell', 'yacine', 'cooper', 'rain']

# for i in range (len(names)):
#     print(i,names[i])

#backward range 
# for i in range(len(names)-1,-1,-1):
#     print (i, names[i])



# -------------------------------- functions --------------

# def greet(name):
#     print(f'hello {name} !')

# greet("mitchell")

# #default params
# def hello(name="Yacine", age=25):
#     print (f"Hello {name} you have {age}")

# hello('mitchell')

# radius = int(input ("Enter the radius "))
# length = int(input ("Enter the length "))


# def area (radius):
#     return (3.142 * radius ** 2)

# def volume (area, legth):
#     return  (area*legth)

# print("volume is :", volume(area(radius),length))





# Scope 

name = "rain"

def name_printer():
    global name 
    name = "mitchell"
    print ("name inside function is", name)


name_printer()
print("name outise of function is", name)