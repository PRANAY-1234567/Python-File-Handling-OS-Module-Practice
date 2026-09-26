import os
print(os.getcwd())


#os.chdir("C:\Users\ASUS\Desktop\Evening class")# To avoid (unicode error) use "r" rastring or chnge single '\' to '\\'


#os.chdir("C:\\Users\\ASUS\\Desktop\\Evening class")# To avoid (unicode error)  change single '\' to '\\


os.chdir(r"C:\Users\ASUS\Desktop\Evening class")# To avoid (unicode error) use "r" rastring 

#os.mkdir('FirstClass')
#os.mkdir('SecondClass')

# os.makedirs("A\B\C\D\E")# To make nested folder or Folder inside folder

# If you want to know 
#print(os.listdir())

# os.rename("FirstClass","Pranay")

# os.popen("Pranay.txt")

# os.rmdir("SecondClass")


# os.remove("Pranay.txt") 

print(os.getcwd())

'''print(file.readable())
#os.popen("marker.txt")
print(file.name)
print(file.mode)
print(file.writable())
file.close()
print(file.closed)'''


file=open("marker.txt","r")
# print(file.read())
'''print(file.readline())
print(file.readline())
print(file.readlines())
print(file.read(4))'''
'''
file1=open("PEN.txt","w")

# file1.write("Hello Guys Jai Hind")
# file1.write("Python Programming")
os.popen("PEN.txt")

file1.writelines(["Python\n","Java\n","SQL\n","PowerBI"])

file2 = open("Walmart.txt","a")

# file2.write("Good Luck\n")
# file2.write("Evening\n")
# file2.write("Ganesh")
file2.writelines(["Python\n","Java\n","SQL\n","PowerBI"])

os.popen("Walmart.txt")
'''

"""file=open("marker.txt","r")
# print(file.read())
print(file.tell())
print(file.seek(4))
print(file.tell())
print(file.readline())
print(file.seek(1))
print(file.tell())
print(file.readline())
"""
'''file=open("marker.txt","r+")
print(file.read())
file.write("*********")
print(file.read())
print(file.tell())
print(file.seek(0))
print(file.read())'''

'''file=open("marker.txt","w+")
print(file.read())
file.write("@@@@@@@@@@@@@@")
print(file.read())
print(file.seek(0))
print(file.read())
'''
file=open("marker.txt","a+")
print(file.read())
file.write("Completed\n")
print(file.read())
print(file.seek(0))
print(file.read())

file.write("Completed\n")
print(file.read())
print(file.seek(0))
print(file.read())