from functions import get_birthdays, get_match

# Display the intro:
print(
    """Birthday Paradox, by Al Sweigart al@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
"""
)

# Set up a tuple of month names in order:
MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

while True:  # Keep asking until the user enters a valid amount.
    print("How many birthdays shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        number_of_birthdays = int(response)
        break  # User has entered a valid amount.
print()

# Generate and display the birthdays:
print("Here are", number_of_birthdays, "birthdays:")
birthdays = get_birthdays(number_of_birthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(", ", end="")

    month_name = MONTHS[birthday.month - 1]
    date_text = f"{month_name} {birthday.day}"
    print(date_text, end="")
print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the results:
print("In this simulation, ", end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    date_text = "{} {}".format(monthName, match.day)
    print("multiple people have a birthday on", date_text)
else:
    print("there are no matching birthdays.")
print()

# Run through 100,000 simulations:
print("Generating", number_of_birthdays, "random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's run another 100,000 simulations.")
sim_match = 0  # How many simulations had matching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = get_birthdays(number_of_birthdays)
    if get_match(birthdays) != None:
        sim_match = sim_match + 1
print("100,000 simulations run.")

# Display simulation results:
probability = round(sim_match / 100_000 * 100, 2)
print("Out of 100,000 simulations of", number_of_birthdays, "people, there was a")
print("matching birthday in that group", sim_match, "times. This means")
print("that", number_of_birthdays, "people have a", probability, "% chance of")
print("having a matching birthday in their group.")
print("That's probably more than you would think!")
