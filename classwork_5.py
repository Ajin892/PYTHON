Python={"Sanjay","Naveen","Kavya"} 
Data_Science={"Sanjay","Akash","Pooja"}
Python.add("Divya")
Data_Science.pop()
print(Python)
print(Data_Science)
print(Data_Science&Python)
print(Python-Data_Science)
print(Python|Data_Science)
course={"Python":"3","Data_Science":3}
for x,y in course.items():
    print("Course:",x,"Students:",y)
expected_growth = {
    course: students * 2
    for course, students in course.items()
}

print("Expected growth:", expected_growth)

   
