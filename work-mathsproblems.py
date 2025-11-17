# Age in 2049
# Author: Marcus Ho
# Date: Nov 14, 2025


def main():
    age = int(input("How old are you now? "))
    future_age = age + 31
    print(f"In 2049 you will be {future_age} years old!")


if __name__ == "__main__":
    main()

    # Olympic Judging
    # Author: Marcus Ho
    # Date: Nov 14, 2025

    def main():
        total = 0
        for i in range(1, 6):
            score = float(input(f"Judge {i}: "))
            total += score
        average = total / 5
        print(f"Your Olympic score is {average:.1f}")

    if __name__ == "__main__":
        main()

        # McDoland's Order Calculator
        # Author: Marcus Ho
        # Date: Nov 14, 2025

        def main():
            total = 0

            burger = input("Would you like a burger for $5? (Yes/No) ").lower()
            if burger == "yes":
                total += 5

            fries = input("Would you like fries for $3? (Yes/No) ").lower()
            if fries == "yes":
                total += 3

            total_with_tax = total * 1.14
            print(f"Your total is ${total_with_tax:.2f}")

        if __name__ == "__main__":
            main()
