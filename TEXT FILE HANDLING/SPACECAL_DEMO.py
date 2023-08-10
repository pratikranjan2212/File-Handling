outF=open("utFile1.txt","w")

# write line to output file
outF.write("122  aas\n")
outF.write("fff      hhh\n")
outF.write("45   r r r")
outF.close()


outF=open("utFile1.txt","r")
outF1=open("utF.txt","w")
s=" "
while s:
    s=outF.readline()
    s1=s.split()
    #print(s1)
    for i in s1:
        outF1.write(i)
        outF1.write(" ")
    outF1.write('\n')
outF.close()
outF1.close()

outF1=open("utF.txt","r")
str=outF1.read()
print(str)
outF1.close()
