#Remove a new file and create csv file
import csv
header=["ID","name","price","qty"]
records=[[102,'LG_Monitor','6500','20'],[103,'Keyboard','1350','156'],
         [105,'HP_Mouse','650','120'],[106,'Speaker','1670','136']]
file=open("product3.csv","w")
found=0
writer=csv.writer(file)
writer.writerow(header)
writer.writerows(records)

if (found==0):
    print(name1,"doesn't exist")
else:
    print(name1,"updated successfully")
file.close()

file=open("product3.csv","r")
data=csv.reader(file)
for record in data:
    print(record)
file.close()    