#Operations of Read() and Write()

# ob=open("stu.txt","w")
# ob.write("Hello!")
# ob.write('\n')
# ob.write("My dear students\n")
# ob.write("This is a text file\n")
# ob.write("For showing you how\n")
# ob.write("File is read in python\n")
# ob.close()

# ob=open("stu.txt","r")
# st=ob.readline()
# st1=ob.readline(3)

# print(st,end=' ')
# print(st1)
# data = ob.read()
# words = data.split()
# print(words)

# print('Number of words in text file :', len(words))
# ob.close()


# st1=ob.read(6)
# print(st1)
# print(ob.read())

#no of words count


#Operations of Readline()

Fileout=open("student1.txt","w")
ans="y"
while ans=='y':
    name=input("enter name of student:")
    Fileout.write(name+'\n')
    ans=input("enter y to continue")
Fileout.close()

Fileout=open("student1.txt","r")
line=0
str=" " 
while str:
    str=Fileout.readline()
    print(str)
    line+=1
print(line)
Fileout.close()


#Operations of Writelines() and readlines()

# Fileout=open("stud.txt","w")
# l=["Sourav kar\n","Satwik Mishra\n","Maxi Mimansa\n"]
# Fileout.writelines(l)

# Fileout=open("stud.txt","r")
# S=Fileout.readlines()
# print(S)
# linecount=0
# wordcount=0
# for i in S:
#    linecount+=1 
#    word=i.split()
#    for j in word:
#       wordcount+=1
# print("No of words",wordcount)
# print("No of line",linecount)
  
# Fileout.close()


# # Opening a file 
# file = open("gfg.txt","r") 
# Counter = 0
  
# # Reading from file 
# Content = file.read() 
# CoList = Content.split("\n")
  
# for i in CoList: 
   
          
# print("This is the number of lines in the file") 
# print(Counter)

#Alternate method

#Q2.Write a program to read the contents from the text file "stu.txt".
#Count the total number of words , lines  and characters present in the text file.

# fname = input("Enter file name: ")
# num_lines = 0
# with open(fname, 'r') as f:
#     for line in f:
#         num_lines += 1
# print("Number of lines:", num_lines)

# file = open("stu.txt", "r")

# number_of_lines = 0
# number_of_words = 0
# number_of_characters = 0
# for line in file:
#   line = line.strip("\n")                  #won't count \n as character
#   print(line)
#   words = line.split()
#   number_of_lines += 1
#   number_of_words += len(words)
#   number_of_characters += len(line)
# print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)
# file.close()






'''ob=open("stu.txt","w")
ob.write("Hello!")
ob.write('\n')
ob.write("A dear students\n")
ob.write("This is a text file\n")
ob.write("A showing you how\n")
ob.write("File is read in python\n")
ob.close()'''

#Q1.WAP to print the number of sentences/lines started with 'i ' in the text file "stu.txt"

# file=open("stu.txt","r")
# lst=file.readlines()
# count = 0 
# for i in lst :
#     words=i.split()
#     for word in words:
#         if word[0]=='i' :
#             print(word)
#             count+=1
# print("So for number words started with i : ",count)
        
# file.close()




  
