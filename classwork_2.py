book1 = "\t{} \t₹{}".format("Python Basics", 450)
book2 = "\t{} \t₹{}".format("Data Science Intro", 600)

total = 450 + 600
Total= "\tTotal price\t{}".format(total)
bill=  book1 + "\n"+ book2 +"\n"+ Total
print(bill.upper())
