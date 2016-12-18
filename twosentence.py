from collections import Counter

sentence1 = input("Please enter a sentence...")

sentence2 = input("Please enter a second sentence...")

list1 = sentence1.split() #splits sentence1 #

list2 = sentence2.split() #splits sentence2 #

print(list1)

print(list2)

list3 = list1 + list2     #combines list 1 and 2#

print(list3)                  #To make list 3#

print(sorted(list1)) # sorts list 1 #

print(sorted(list2)) # sorts list 2 #

print(sorted(list3)) # sorts list 3#

print(len(list1))    # returns length of list1#

print(len(list2))    # returns length of list2#

print(len(list3))    # returns length of list3#

dictionary = dict(Counter(list3)) #creates dictionary and counted list#

print(dictionary)
