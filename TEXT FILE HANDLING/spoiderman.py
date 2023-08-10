myfile=open('C:\\Users\\Home\\Desktop\\PYTHON\\TEXT FILE HANDLING\\spiderman.txt','r')
lst=myfile.readlines()
print(lst)
count=0
for line in lst:
    if line.startswith('I'):
        count+=1
    elif line.startswith('i'):
        count+=1

print("No of lines starting with 'I' - ",count)