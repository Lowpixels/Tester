# Numbers and Operations
# Author: Marcus Ho
# 5 November 2025
# Create an algorithm to gather
# data to find the most popular
# bubble tea place around us
# Version 1
# Show all the bbt choices
# Ask the user for their choice
# Add their vote to a running
# tally
# Give some raw scores
# Give score as a percentage
# Version 2
# Ask the user what their fave
# bbt place is
# Add their vote to a running
# tally
# Give the raw score
# Give score as percentage
def vote_open_choice():
    """Keeps track dynamically of user's choice.
    Note: choices must match text exactly (case is not sensitive)"""

    votes = {}          # holds vote information    key     -> value
                        #                           place   -> num votes

    for _ in range(NUM_VOTERS):
        # Ask the user what their fave
        os.system("clear")
        cur_vote = input("What's your favourite local bubbble tea cafe? ").lower().strip(",.?! ")

        # Checks if current place is in the votes dictionary
        # If it doesn't exist, initialize the key-value pair
        if cur_vote not in votes:
            votes[cur_vote] = 1
        else:
            votes[cur_vote] += 1

    # Print the results
    print("-------------------------------------")
    print("Results:")

    # By default, iterating over a dictionary gives you the keys
    for place in votes:
        # Print the raw score and percentage for each key in the dictionary
        percentage = votes[place] / NUM_VOTERS * 100

        print(f"{place.capitalize()} votes: {votes[place]} | percentage: {percentage}% of the vote")

    print("-------------------------------------")

