import datetime
import random
from typing import List


def get_birthdays(number_of_birthdays: int) -> List[datetime.date]:
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for _ in range(number_of_birthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        random_number_of_days = datetime.timedelta(random.randint(0, 364))

        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)

    return birthdays


def get_match(birthdays: List[datetime.date]):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthday_A in enumerate(birthdays):
        for _, birthday_B in enumerate(birthdays[a + 1 :]):
            if birthday_A == birthday_B:
                return birthday_A  # Return the matching birthday.
