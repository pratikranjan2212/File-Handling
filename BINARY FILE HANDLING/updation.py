import pickle
def write():
    f=open("BinaryFile.dat",'wb')
    while True:
        roll=int(input("Enter roll no:"))
        name=input("Enter Name:")
        per=(float(input("Enter percentage:")))
        R=[roll,name,per]
        pickle.dump(R,f)
        ch=input('more records?')
        if ch=='n' or ch=='N':
            break
        
    f.close()

def read():
    file=open("BinaryFile.dat",'rb')
    try:
        while True:
            rec=pickle.load(file)
            print(rec)
    except EOFError:
        file.close()

def Update():
    with open("BinaryFile.dat",'rb+') as f:
        a=int(input("Enter roll no to be updated:"))
        pos=0
        found=0
        try:
            while True:
                pos=f.tell()
                r=pickle.load(f)
                if r[0]==a:
                    r[2]=float(input("Enter new percentage:"))
                    f.seek(pos)
                    pickle.dump(r,f)
                    found+=1
                    print(r)
        except EOFError:
            f.close()

write()
read()
Update()