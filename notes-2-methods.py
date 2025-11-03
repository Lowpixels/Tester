# (string) methods
# Author: Marcus
# 6 Oct 2025

# Ask the user what the weather is like
weather = input("What is the weather like today? ")
if weather.lower().strip("!") == "rainy":
   # rainy, RAINY, RAiny
   print("You should bring an umbrella.")
else:
    print("I see..)")
    # ask the customer if they want fries
    fries_reply = input("Do you want fries?") # "yes!"

    if "yes" in fries_reply.lower:
        print("Here are your fries.")
    else:
        print("OK, You'll not have fries.")
