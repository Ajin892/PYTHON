nstudent=int(input("number of student:"))
for i in range(0,nstudent):
    stu1=input("name:")
    a=open("t.txt","a")
    a.write(stu1+"\n")
a.close()
ab=open("t.txt","r")
abc=ab.read()
print(abc)
    