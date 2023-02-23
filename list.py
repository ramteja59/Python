#list
l=[10, 'ramteja', 1.22, True]    #list holds diffrerent data types
print(l[2])
f=[10, 10, 'ram', 'ram', 'teja']   #list can accept duplicate values
print(f[1:4:1])
print(f[-2])
print(type(f))  #for finding class type
#list methods
#append() - to add an element at last of the list
f.append(400) #add element at end of list
print(f)
f.insert(1, 'moolya') #insert - replaced moolya in index 1
print(f)
f.remove('ram') #remove method
f.remove('ram')
print(f)
#sorting
a= ['c','d','g','z','q', 'd']
a.sort()
print(a)
b=[22,58,36, 100, 1]
b.sort()
b.reverse() #revrse - decending order
#b.sort(reverse=True) #decending order
b.clear() #to clear/empty
print(b)
print(a.count('d'))
