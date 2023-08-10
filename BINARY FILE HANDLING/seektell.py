f=open('s1.txt','w')
f.write('123456789\n')
f.write('1234567\n')
f.write('1234\n')
f.close()

f=open('s1.txt','rb')
print(f.tell())

f.seek(3)
print(f.tell())

print(f.read(2))
print(f.tell())

f.seek(3,1)
print(f.tell())

f.seek(-4,2)
print(f.tell())
print(f.read(2))
print(f.tell())
f.close()