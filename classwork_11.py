try:
    book=input("book title=")
    year=(input("publication year="))
    if book.isalpha() or book.isspace():
        raise ValueError ("only alphabhet and spaces")
    else:
        print("")
    
    if (year.startswith("19")) or (year.startswith("20")):
        print("")
    else:
        raise ValueError("year only start with 19 or 20")

except ValueError as e:
    print("Error:", e)

finally:
    print("Library system check completed.")