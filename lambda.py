nums = [1,2,3,4,5,6]
def square(n):
    return n**2



# print (list(map(square,nums)))


# <============>

print (list(map(lambda n: n**2,nums)))

# lambda works with map and filter 