import random
import math
nstudent=int(input("number of customer:"))
friend_list=[]
for i in range(0,nstudent):
    stu1=input("name:")
    friend_list.append(stu1)
    
print("name of friends",friend_list)
win=[random.choice(friend_list),random.choice(friend_list)]
print("Random element from list:",win)
def reverse(string1,string2): 
    string1= "".join(reversed(string1))
    string2="".join(reversed(string2))
    print("reversed name:",string1)
    print("reversed name:",string2)
reverse(win[0],win[1])
print("number of frinds",nstudent)
print("square root",math.sqrt(nstudent))
print("nearest to whole nummber",math.floor(math.sqrt(nstudent)))