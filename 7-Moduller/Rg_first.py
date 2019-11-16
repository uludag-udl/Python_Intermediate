import os

os.startfile("www.google.com.tr") #Google'a git

print(os.name) # output => "nt" for windows // "posix" for MacOs and GNU/linux

print(os.sep) #output => "\\" for Windows // "/" for MacOs and Linux 

liste=["bear","cat","dog"]
a=os.sep.join(liste)
print(a)  #=> output :   bear\cat\dog

