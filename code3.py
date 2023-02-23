a = 5
print(a ** 3)

# presidence of operators
print(5 + 8 - 2)
# String manupulation
str1 = "ramteja"
print(len(str1))
print(str1[3])
# covert int into string
b = 3456
print(str(b))
print(type(b))
# operation in strings
# find
print(str1.find("t"))  # to find
print(str1.find("z"))
print(str1.upper())
print(str1)
print(str1.count("j"))
print(str1.islower())  #check case
str2 = " hello "
print(str2)
print(str2.strip())  #removing space
str3 = " vishakapatnam "
print(str3.replace("v", "b"), str3.upper())
print(str3.replace("a", "s").upper())
print(str3.lstrip())  #space for left side
print(str3.rstrip()) #space for right side
#split operation
str4 = "Executable module that opens up a browser instance and runs the test script"
print(str4.split("e"))
print(str4.split("module"))
str5 = "ram\" teja" #escapde character - for quote between names
print(str5)
x= """
sushanth is excellent teacher
"""
print(x)
print('is' in x)

