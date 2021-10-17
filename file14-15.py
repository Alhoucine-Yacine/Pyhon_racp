#------------------------ dictionaries ----------------------

# dict = {"name1" : "mitchell",
#         "name2" : "yacine",
#         "name3" : "rain"}

# #print value of a key
# print(dict['name1'])


# #print true if present in dict (key)
# print ("name1" in dict)

# #print keys of dict 
# print(dict.keys())

# #print keys of dict on list
# print(list(dict.keys()))

# #print values of dict 
# print(dict.values())

# #print values of dict on list
# print(list(dict.values()))

# # count by values 
# vals = list(dict.values())
# print (vals.count('yacine'))
# print (vals.count('yacinee'))

# dict['name4']="cooper"
# print (dict)


# create object of type dict 
# person = dict (name="yacine",age="25")
# print (person)


# ---------------------- use dicts in prog ----------------
# def dictLister(localDict):
#     for key,val in localDict.items() :
#         print (f'I am {key} and my rank is {val}') 

def countRank(localdict):
    ranks = list(localdict.values())
    # we use set in next line to prevent duplicating printing the same line twice
    for rank in set(ranks):
        num = ranks.count(rank)
        print (f'there are {num} of {rank}' )

myDict = {}

while True:
    name=input('you name : ')
    rank=input('your rank : ')
    myDict[name] = rank

    another = input ('add another ? (y/n')
    if another == 'y':
        continue
    else:
        break 

countRank(myDict)

# dictLister(myDict)




