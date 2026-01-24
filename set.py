a={2,3,4,5}
print(a.add(6),a) #add 6 to the set
print(a.remove(3),a) #remove 3 from the set         
print(a.pop(),a)  #it is going to remove a random element
print(a.union({7,8,9})) #it will add 7,8,9 from the set and return a new set
print(a.clear(),a) #it will clear the set and return a new set
print(a.update({10,11,12}),a) #it will add 10,11,12 to the set  
print(a.intersection({4,5,6,7})) #it will return the common elements from both the sets
print(a.difference({4,5,6,7})) #it will return the elements which are not common in both the sets
print(a.symmetric_difference({5,6,7,8})) #it will return the elements which are not common in both the sets
print(a.issubset({2,4,5,6,10,11,12})) #it will return true if all elements of set a are present in the given set
print(a.issuperset({2,4})) #it will return true if all elements of given set are present in set a
print(a.isdisjoint({13,14,15})) #it will return true if both the sets have no common elements
print(len(a)) #it will return the length of the set
print(2 in a) #it will return true if 2 is present in the set otherwise false
print(20 not in a) #it will return true if 20 is not present in the set otherwise false
print(a.copy()) #it will return a copy of the set
print(a)
print(frozenset(a)) #it will return an immutable set
#frozenset is an immutable set means we cannot change the elements of the set
print(a)
print(type(a)) #it will return the type of the set
#sets are unordered collection of unique elements
#sets are mutable means we can change the elements of the set
#frozenset is an immutable set means we cannot change the elements of the set
#frozenset is immutable means we cannot add or remove elements from the set
#sets are defined by curly braces {}
#frozenset is defined by frozenset() function
print(set([1,2,3,4,5])) #it will return a set from the given list
print(set((1,2,3,4,5))) #it will return a set from the given tuple
print(set({1: 'a', 2: 'b', 3: 'c'})) #it will return a set from the given dictionary keys   
print(a)#it will return a set from the given dictionary keys
