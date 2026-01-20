# Big Data
# Author: Marcus
# 17 November 2025

# Open files using Python
# Read the data in the files
# Interpret the data that we read


def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
    # Read the file
    header_row = file.readline()

    # Get information about the fave pizza place
    uncle_fatihs = 0
    club_ilia = 0
    pizza_hut = 0

    # Get info for fave burrito
    guadalupe = 0
    quesada = 0

    for line in file:
        # fave pizza is in column 5 (4 index)
        # each line is a string
        # split the string wherever a , is
        # convert from string -> list
        info = line.split(",")
        fave_pizza = info[4]
        fave_burrito = info[5]

        if fave_pizza == "Uncle Fatih's":
            uncle_fatihs += 1
        elif fave_pizza == "Club Ilia":
            club_ilia += 1
        elif fave_pizza == "Pizza Hut":
            pizza_hut += 1

        if fave_burrito == "Guadalupe (MBC)":
            guadalupe += 1
        elif fave_burrito == "Quesada (Cornerstone)":
            quesada += 1

    # Display results
    print("------------------")
    print("Results:")
    print(f"Uncle Fatih's votes: {uncle_fatihs}")
    print(f"Club Ilia votes: {club_ilia}")
    print(f"Pizza Hut votes: {pizza_hut}")

    if guadalupe > quesada:
        print("Guadalupe is the most popular burrito!")
    elif quesada > guadalupe:
        print("Quesada wins most popular burrito!")
    else:
        print("It's a tie between Guadalupe and Quesada.")

    print("------------------")

    file.close()


if __name__ == "__main__":
    main()
