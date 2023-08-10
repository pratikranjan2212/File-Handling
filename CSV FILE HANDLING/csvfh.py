import csv
#writing
f=open("emp2.csv","w")
ch="y"
lst=[]
while ch=="y":
    rollno=input("Enter roll no.")
    name=input("Enter name:")
    stream=input("Enter stream:")
    fees=input("Enter fees:")
    records=[rollno,name,stream,fees]
    lst.append(records)
    csvwriter=csv.writer(f,lineterminator="\n")
    csvwriter.writerows(lst)
    ch=input("WANT MORE RECORDS:")
f.close()
print("Record added:")

#reading
file=open("emp2.csv","r")
data=csv.reader(file)
for record in data:
    print(record)
file.close()

#Searching operation
f=open("emp2.csv","r")
rollno1=input("Enter roll no. u want to search:")
data=csv.reader(f)
found=0
for rec in data:
    if rec[0]==rollno1:
        print(rollno1,"found in your csv file")
        print(rec)
        found=1
        break
if (found==0):
    print("bye")
f.close()


