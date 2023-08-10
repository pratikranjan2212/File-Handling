import csv
header = ['ID','name','Price','Qty']           
records=[[102,'LG_Monitor','6500','20'],[103,'Keyboard','1350','156'],
         [105,'HP_Mouse','650','120'],[106,'Speaker','1670','136']]

#write
f=open('Invent.csv','w')
csvwriter=csv.writer(f,lineterminator='\n',delimiter=',')
csvwriter.writerow(header)
csvwriter.writerows(records)
f.close()
print('Check ur file now...')

#read
f=open('Invent.csv','r')                       
data=csv.reader(f)

for rec in data:
    print(rec)
f.close()

#updation
file=open('Invent.csv','r')
records=[]
reader1=csv.reader(file)
name1=input("Name to update:")
found=0
for line in reader1:
    if line[1]==name1:
        line[1]=input("Enter New name:")
        records.append(line)
        found=1
    else:
        records.append(line)

#Remove a current file and create new csv file
if (found==0):
    print(name1,"doesn't exist")
else:
    print(name1,"updated successfully")
file.close()

file=open("Invent.csv","r")
data=csv.reader(file)
for record in data:
    print(record)
file.close()


