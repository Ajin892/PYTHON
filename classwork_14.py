import random
import math
nstudent=int(input("number of friends:"))
friend_list=[]
for i in range(0,nstudent):
    stu1=input("name:")
    friend_list.append(stu1)
    
print("name of friends",friend_list)
win=random.choice(friend_list)
print("Random element from list:",win)
def reverse(string): 
    string = "".join(reversed(string)) 
    return string 
print("reversed name:",reverse(win))
print("number of frinds",nstudent)
print("square root",math.sqrt(nstudent))
print("nearest to whole nummber",math.floor(math.sqrt(nstudent)))