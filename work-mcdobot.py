# work-mcdobot.py

answer = input("Would you like fries with your meal? (Yes/No) ").strip().lower()

if answer in ("yes", "y"):
    print("Here's your meal with fries!")
elif answer in ("no", "n"):
    print("Here's your meal without fries!")
else:
    print(f"Sorry. I don't understand {answer}.")
