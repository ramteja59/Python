#multiline
str="""Selenium is an open-source tool that automates web browsers. 
It provides a single interface that lets you write test scripts in programming languages like 
Ruby, Java, NodeJS, PHP, Perl, Python, and C#, among others.
"""
print(str[::-1]) #reverse
print(str[0])
print(str[2])
print(str[-2])
print(str[0:7])
print(str[9:11])
print(str[::1])  #for whole sentence
print(str[0:])
print(str[-9:-1])
print(str.find("tool")) #find the element