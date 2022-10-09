"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday problem
This version of the algorithm is written by Igor Bondar ibondar.altilan@gmail.com
leaps years also me be included
Tags: short, math, simulation
"""

import datetime
import random
from collections import Counter

# constants definition
MAX_BIRTHDAYS = 100  # max birthdays in the testing group
PRINT_FORMAT = 10    # define a number of values while birthdays list is printing
SIMULATION_NUMBER = 100_000   # group simulation SIMULATION_NUMBER times
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

DAYS_IN_YEAR = 365  # without leap years
# DAYS_IN_YEAR = datetime.date.max.toordinal()  # include leap years


def generate_date_list(length, days_in_year):
    """Return a date list with length as strings 'Mth DD', 'Mth D"""
    result = []
    for i in range(length):
        ordinal_date = random.randrange(1, days_in_year)    # get random day of a year
        date = datetime.date.fromordinal(ordinal_date)  # get object of the date type
        string_date = MONTHS[date.month - 1] + ' ' + str(date.day)  # convert Month + Day to a string
        result.append(string_date)  # add to list
    return result


def check_match_birthdays(birthdays):
    """Return an object of Counter() like dict {date, number) of matching birthdays"""
    count = Counter()
    for x in birthdays:
        count[x] += 1
    return count

def print_birthdays_list(birthdays):
    """output birthdays list in a humane readable format 'Mth D', 'Mth DD'
    {PRINT_FORMAT} items on each line"""
    i = 1
    for x in birthdays[:len(birthdays) - 1]:
        if i % PRINT_FORMAT != 0:
            print(x, end=', ')
        else:
            print(x)
        i += 1
    print(birthdays[len(birthdays) - 1])
    print()


def main():
    # input a number of birthdays in the test group
    while True:
        birthdays_number = input(f'How many birthdays shall I generate? (Max {MAX_BIRTHDAYS}) \n> ')
        if birthdays_number.isdigit() and int(birthdays_number) <= MAX_BIRTHDAYS:
            break                                     # input is OK
        else:
            print(f'Enter a number not over {MAX_BIRTHDAYS}')

    """prepare a dict for each day of the leap year = 366 days,
    keys are strings like 'MthNN', for example: Mar06,
    values are a number of birthdays for that date,
    initialise values the dict to zero, and keys from all_days list
    """

    birthdays = generate_date_list(int(birthdays_number), DAYS_IN_YEAR)   # generate a sample birthdays list
    count = check_match_birthdays(birthdays)              # get an instance of Counter() as {date, number}
    matches = {k: v for (k, v) in count.items() if v > 1}   # get matched birthdays as a dict {date, if number > 1}
    # print n birthdays and comment the result
    print(f'Here are {birthdays_number} birthdays:')
    print_birthdays_list(birthdays)
    if not matches:
        no_matches = 'no'
    else:
        no_matches = 'a'
    print(f'In this simulation, multiple people have {no_matches} birthday on: {", ".join(matches.keys())}')

    # generating an array of birthdays
    print()
    input(f'Generating {birthdays_number} random birthdays {SIMULATION_NUMBER:,} times\n'
          f'Press Enter to begin...')

    # main loop
    result = 0
    for i in range(SIMULATION_NUMBER):

        if i % 10_000 == 0:
            print(f'{i:,} simulation run...')   # comma ',' as separator of thousands

        birthdays = generate_date_list(int(birthdays_number), DAYS_IN_YEAR)   # get a new birthdays list
        count = check_match_birthdays(birthdays)              # get matched birthdays as a Counter {date, number}
        if count.total() > len(count):                        # at least one number > 1
            result += 1
    # end of loop
    print(f'{SIMULATION_NUMBER:,} simulation run...')             # print total number of simulation
    # output and comment results
    percentage = result / SIMULATION_NUMBER
    print()
    print(f'Out of {SIMULATION_NUMBER:,} simulations of {birthdays_number} people, there was\n'
          f'a matching birthday in that group {result} times. This means\n'
          f'that {birthdays_number} people have a {percentage:2.2%} chance of\n'
          f'having a matching birthdays in their group.')


if __name__ == '__main__':
    main()