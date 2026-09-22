try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if name == "":
        raise ValueError("Name cannot be empty.")

    if feedback == "":
        raise ValueError("Feedback cannot be empty.")

    print("Thank you,", name)
    print("Your feedback:", feedback)

except ValueError as e:
    print("Error:", e)

finally:
    print("Feedback process completed.")