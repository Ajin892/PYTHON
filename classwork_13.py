item=input("new items:")
a=open("test.txt","a")
a.write(item+"\n")
a.close
ab=open("test.txt","r")
abc=ab.read()
print(abc)

