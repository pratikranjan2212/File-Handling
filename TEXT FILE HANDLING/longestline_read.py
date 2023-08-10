#reading longest line 
f1=open("C:\\Users\\Home\\Desktop\\PYTHON\\TEXT FILE HANDLING\\longest.txt","r")
str=f1.readline()
max=len(str)
s=str
while str:
    str=f1.readline()
    if len(str)>max:
        s=str
        max=len(str)
f1.close()
print("longest line is :")
print(s)
