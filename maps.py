from random import shuffle

words = ["mitchell","yacine","rain"] 

listt=[]



def jumble(word):
    anagram =  list(word)
    shuffle(anagram)
    return ''.join(anagram)

# for word in words:
#     listt.append(jumble(word))

# <=====>

print(list(map(jumble, words)))


# <=====>

print([ jumble(word) for word in words])