#Notes - Introduction
# 16 September
# Marcus Ho

import time

# Create an algorithm to solve a problem
# Problem: create our own chatbot
#           MeCPT

# 1. Greet the user with a predetermined statement
greeting = "Hello, I am a chatbot."
print(greeting)

#2
print("My name is MeGPT, ")
print("I'M NOT LIKE THE OTHER GUY.")
print("I am completely deterministic.")

# 3. Wow the user with some maths
print("I bet you don't know what 8x8 is.")
print("Ican do it.")
print(f"8x8 is actually {8*8}")

print("What is pi squared?")
print("I'm smart, I can do it too.")
print(f"It is {3.14159265359 ** 2}.")

# 4 Make the bot crash out a little bit.
print(" The quick brown fox jumps over the lazy dog" * 10)


# get name of user
username = input("What is your name?")

time.sleep(1)

print(f"Wow {username}, that is a cool name")

time.sleep(2)

q1 = input("Anyways, What is your favourite food?")

time.sleep(1)

print(f"I would say {q1} is good, however I like korean corn cheese with extra cheese")

time.sleep(2)

q2 = input("I would like to get to know you a little bit more. Tell me your favourite sport.")

time.sleep(1)

print(f"{q2} sounds interesting, my favourite sport is badminton.")

time.sleep(1)

q3 = input("Why do you like this sport?")

time.sleep(1)

print(f"your reasoning of '{q3}' sounds interesting thank you for sharing!")

time.sleep(1)

print("Wow, sounds interesting. Thank you for your time. It has been a pleasure. See you later! - MeGPT")
