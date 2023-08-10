outF=open("sports.txt","w")

  # write line to output file
outF.write("Atheletic~geetanjali\n")
outF.write("singer~madhav\n")
outF.write("atheletic~sipun\n")
outF.write("Musician~sipun")
outF.close()



f1=open("sports.txt","r")
f2=open("atheletic.txt","w")
s=" "
while s:
    s=f1.readline()
    s1=s.split('~')
    if s1[0].lower()=='atheletic':
        f2.write(s+'\n')
    
    print(s1)
f1.close()
f2.close()
f2=open("atheletic.txt","r")
r=f2.read()
print(r)
f2.close()
