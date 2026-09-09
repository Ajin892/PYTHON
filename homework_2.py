cha = """Learn Python programming from
basics to advanced concepts
through practical projects"""
length = len(cha)
first = cha[0]
last = cha[-1]
sli = cha[:50]
chac = cha.lower()
replace1 = chac.replace("Python", "PYTHON")
a = chac.strip()
list1 = a.split()
print(length)
print(first)
print(last)
print(sli)
print(a)
print(list1)
b = "course" in a
if b:
    print("course in paragraph")
print("The course description is {} characters long and has {} words.".format(
    length, len(list1)
))



