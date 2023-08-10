#Writing employee record

f3=open("records.txt","w")
ans='y'
while ans=='y' or ans=='Y':
    l=[]
    name=input("entr name")
    l.append(name+'\t')
    occu=input("entr occu")
    l.append(occu+'\t')
    age=input("entr age")
    l.append(age+'\n')
    f3.writelines(l)
    ans=input("enter y to cont")
f3.close()

#reading records
f3=open("records.txt","r")
s=f3.readlines()
print("Name   Occupation   Age")
for line in s:                          
      x=line.split()
      if int(x[2])>0:
          print(line,end="")
f3.close()
