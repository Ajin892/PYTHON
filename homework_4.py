Web_Development = ["Rahul", "Priya", "Arjun"]
Data_Science = ["Sneha", "Karthik", "Ananya"]
UIUX_Design = ["Vikram", "Neha", "Rohan"]
all_participants = [Web_Development, Data_Science, UIUX_Design]
Web_Development.append("Sanjay")
Data_Science.insert(1, "Divya")
UIUX_Design.pop()
Data_Science_copy = Data_Science.copy()
Data_Science.clear()
print("First two Web Development participants:", Web_Development[:2])
length = [len(name) for name in Data_Science_copy]
print("Name lengths:", length)
if "Asha" in Web_Development or "Asha" in Data_Science_copy or "Asha" in UIUX_Design:
    print("Asha is a participant")
else:
    print("Asha is not a participant")
first_participants = (
    Web_Development[0],
    Data_Science_copy[0],
    UIUX_Design[0]
)
print("First participants:", first_participants)