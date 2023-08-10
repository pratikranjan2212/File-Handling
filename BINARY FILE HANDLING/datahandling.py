# #1
# import pickle
# f=open("binary.dat",'wb')
# l=[]
# ans='y'

# while ans=='y':
#     roll=int(input("Enter Student Roll:"))
#     l.append(roll)
#     name=input("Enter Student Name:")
#     l.append(name)
#     mark=[]
#     for i in range(0,2):
#         x=float(input("Enter marks:"))
#         mark.append(x)
#     l.append(mark)
#     ans=input("Enter y to continue:")

# pickle.dump(l,f)
# f.close()
# f=open("binary.dat",'rb')
# l=pickle.load(f)
# print(l)
# f.close()

# #2
# import pickle
# file=open("student.dat","wb")
# lst=[]
# while True:
#     roll=input("Enter Student Roll No:")
#     sname=input("Enter Student Name:")
#     student=[roll,sname]
#     lst.append(student)
#     choice=input("Want to add more record(y/n):")
#     if (choice=='n'):
#         break
# pickle.dump(lst,file)
# file.close()

# file=open("student.dat",'rb')
# try:
#     while True:
#         lst=pickle.load(file)
#         print(lst)
# except EOFError:
#     file.close()

# #3
# import pickle
# def Search():
#     with open("student.dat","rb") as f:
#         found=0
#         rollno=int(input("Enter Roll No to be searched:"))
#         try:
#             while True:
#                 r=pickle.load(f)
#                 if r[0]==rollno:
#                     print("record found")
#                     print(r)
#                     found=1
#                     break
#         except EOFError:
#             f.close()
#         if found==0:
#             print("sorry")
# Search()

# #4
# import pickle
# output_file=open("myfile.dat","wb")
# myint=42
# mystring="Hello World"
# mylist=["dog","cat","lizard"]
# mydict={"name":"Bob","job":"Astronaut"}

# #WRITING RECORDS FROM BINARY FILE
# pickle.dump(myint,output_file)
# pickle.dump(mystring,output_file)
# pickle.dump(mylist,output_file)
# pickle.dump(mydict,output_file)

# output_file.close()

# #READING RECORDS FROM BINARY FILE
# output_file=open("myfile.dat","rb")

# myint=pickle.load(output_file)
# print(myint,type(myint))
# mystring=pickle.load(output_file)
# mylist=pickle.load(output_file)
# mydict=pickle.load(output_file)

# #PRINTING RECORDS TO BINARY FILE
# print('myint=',myint)
# print("mystring=",mystring)
# print("mylist=",mylist)
# print("mydict=",mydict)

# #5
# import pickle
# def write():
#     f=open("BinaryFile.dat",'wb')
#     Rec=[]
#     while True:
#         roll=int(input("Enter roll no"))
#         name=input("Enter Name:")
#         per=(float(input("Enter percentage:")))
#         R=[roll,name,per]
#         Rec.append(R)
#         ch=input('more records')
#         if ch=='n' or ch=='N':
#             break
#     pickle.dump(Rec,f)
#     f.close()

# def read():
#     f=open("BinaryFile.dat",'rb')
#     Rec=pickle.load(f)
#     print(Rec)
#     f.close()

# def Search():
#     with open("BinaryFile.dat",'rb') as f:
#         a=int(input("Enter roll no to be searched:"))
#         Rec=pickle.load(f)
#         found=0
#         for i in Rec:
#             if i[0]==a:
#                 print('Record found')
#                 print(i)
#                 found+=1
#         if found==0:
#             print('File not found')

# write()
# read()
# Search()

#6
import pickle
def write():
    f=open("BinaryFile.dat",'wb')
    while True:
        roll=int(input("Enter roll no"))
        name=input("Enter Name:")
        per=(float(input("Enter percentage:")))
        Rec={'roll':roll,'name':name,'per':per}
        pickle.dump(Rec,f)
        ch=input('more records')
        if ch=='n' or ch=='N':
            break
    f.close()
 
def read():
    f=open("BinaryFile.dat",'rb')
    try:
        while True:
            Rec=pickle.load(f)
            print(Rec)
    except EOFError:
        f.close()
        print('The end')

def Search():
    f=open("BinaryFile.dat",'rb')
    a=int(input("Enter roll no to be searched:"))
    found=0
    while True:
        try:
            rec=pickle.load(f)
            if rec['roll']==a:
                print('Record found')
                print(rec)
                found=1
        except EOFError:
            f.close()
        if (found==0):
            print('Record not found')
            f.close()

        
def Update():
    F=open('BinaryFile.dat','rb+')
    rnm=int(input("Roll no to be updated:"))
    Pos=0
    found=0
    try:
        while True:
            Pos=F.tell()
            r=pickle.load(F)
            if r['roll']==rnm:
                r['per']=float(input('Enter new percentage:'))
                F.seek(Pos)
                pickle.dump(r,F)
                found+=1
    except EOFError:
        F.close()
# write()
read()
Search()
# Update()
# read()
