# d={i:"a" for i in range(1,5)}
# print(d)
d={1:"a",2:"b",3:"c"}
print(d.keys()) #it will return the keys of the dictionary
print(d.values()) #it will return the values of the dictionary
print(d.items()) #it will return the key-value pairs of the dictionary as tuples in a list
for i in d.items():
    print(i) #it will return the key-value pairs of the dictionary as tuples
for i,j in d.items():
    print(i,j) #it will return the key-value pairs of the dictionary
print(d.get(2)) #it will return the value of the key 2
print(d.get(5,"Not Found")) #it will return "Not Found" as key 5 is not present in the dictionary
d.update({4:"d"}) #it will add the key-value pair 4:"d to the dictionary
print(d)    
print(d.pop(3)) #it will remove the key-value pair with key 3 and return its value
print(d)    
print(d.popitem()) #it will remove and return the last key-value pair as a tuple
print(d)
d.setdefault(5,"e") #it will add the key-value pair 5:"e" to the dictionary if key 5 is not present
print(d)    
d.setdefault(2,"z") #it will not change the value of key 2 as it is already present
print(d)    
d1={"x":"p","y":"q"}
d.update(d1) #it will add the key-value pairs from d1 to d  
print(d)  
d.clear() #it will clear the dictionary         
print(d)
d={1:"a",2:"b",3:"c"}
print(len(d)) #it will return the length of the dictionary
print(2 in d) #it will return true if key 2 is present in the dictionary otherwise false
print(5 not in d) #it will return true if key 5 is not present in the dictionary otherwise false
print(d.copy()) #it will return a copy of the dictionary    
print(d)
print(type(d)) #it will return the type of the dictionary
#dictionaries are unordered collection of key-value pairs
#dictionaries are mutable means we can change the elements of the dictionary    
#dictionaries are defined by curly braces {}
print(dict([(1,"a"),(2,"b"),(3,"c")])) #it will return a dictionary from the given list of tuples
print(dict({1:"a",2:"b",3:"c"})) #it will return a dictionary from the given dictionary
print(dict(x=10,y=20,z=30)) #it will return a dictionary from the given key-value pairs 
print(d) #it will return the dictionary 
