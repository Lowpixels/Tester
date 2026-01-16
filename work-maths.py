# Maths Stuff with Python
# Author: Marcus
# 12 November 2025

# Coffee Affordability Calculator
# Calculate how many coffees you can afford with your budget
# and how much money you'll have left over!


def calculate_coffees(budget: float, coffee_price: float) -> tuple:
    """Calculate number of coffees affordable and remaining money."""
    num_coffees = int(budget // coffee_price)
    remaining = budget - (num_coffees * coffee_price)
    return num_coffees, remaining


def main():
    print("☕ Coffee Affordability Calculator ☕")
    print("=" * 40)

    budget = float(input("How much money do you have? $"))
    coffee_price = float(input("How much does one coffee cost? $"))

    num_coffees, remaining = calculate_coffees(budget, coffee_price)

    print("\n" + "=" * 40)
    print(f"You can buy {num_coffees} coffees! ☕" * min(num_coffees, 5))
    print(f"You'll have ${remaining:.2f} left over.")

    if num_coffees == 0:
        print("😢 Not enough for even one coffee!")
    elif num_coffees >= 10:
        print("🎉 That's a LOT of coffee! Stay caffeinated!")
    else:
        print("😊 Enjoy your coffee!")


if __name__ == "__main__":
    main()
