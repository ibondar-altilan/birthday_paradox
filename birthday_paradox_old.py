"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday problem
Tags: short, math, simulation
"""

import datetime
import random

MAX_BIRTHDAYS = 100  # max birthdays in the testing group
PRINT_FORMAT = 10    # define a number of values while birthdays list is printing
SIMULATION_NUMBER = 100000   # group simulation SIMULATION_NUMBER times


# inpit q-ty of birthdays to generate (max 100)
# birthdays_number


def get_string_date(date_as_ordinal):
    """Return string date 'MthNN' from date_as_ordinal """
    date = datetime.date.fromordinal(date_as_ordinal)  # object of the date type
    month = f'{date:%b}'  # fetch a month as 'Mth'
    day = f'{date:%d}'  # fetch a date as 'NN'
    return month + day


def generate_date_list(date_method, len):
    """Return a date list with length=length as strings 'MthDD in range or random orders"""
    result = []
    for i in range(1, len+1):
        ordinal_date = date_method(i) + i               # get ordinal in range or random
        # print(ordinal_date)                           # for debug
        string_date = get_string_date(ordinal_date)
        result.append(string_date)
    return result


def get_random(birthdays_number):
    return random.randrange(1, datetime.date.max.toordinal() - birthdays_number)    # do not over the max ordinal date


def print_birthdays_list(birthdays):
    """output birthdays list in a humane readable format MthNN, MthNN
    {PRINT_FORMAT} items on each line"""
    i = 1
    for x in birthdays:
        if i % PRINT_FORMAT != 0:
            print(x, end=' ')
        else:
            print(x)
        i += 1
    print()

# print n birthdays, comment it

# generate n random birthdays 100_000 times
    # print the number of every 10_000 iteration

# calculate the number of matching birthdays in this group
# calculate the percentage of matching
# print results

# ask to repeat calculations

def main():
    while True:
        birthdays_number = input(f'How many birthdays shall I generate? (Max {MAX_BIRTHDAYS}) \n> ')
        if birthdays_number.isdigit() and int(birthdays_number) <= MAX_BIRTHDAYS:
            break                                     # input is OK
        else:
            print(f'Enter a number not over {MAX_BIRTHDAYS}')

    print(birthdays_number)
    """prepare a dict for each day of the leap year = 366 days,
    keys are strings like 'MthNN', for example: Mar06,
    values are a number of birthdays for that date,
    initialise values the dict to zero, and keys from all_days list
    """
    all_days = generate_date_list(lambda x: 0, 1500)    # 1500 days cover more than 4 year, so leap year included
    results = dict.fromkeys(all_days, 0)
    print(len(results))

    # generate sample birthdays list
    birthdays = generate_date_list(get_random, int(birthdays_number))

    # print n birthdays
    print(f'Here are {birthdays_number} birthdays:')
    print_birthdays_list(birthdays)

    # generating an array of birthdays
    print()
    input(f'Generating {birthdays_number} random birthdays {SIMULATION_NUMBER} times\n'
          f'Press Enter to begin...')
    # main loop
    for i in range(SIMULATION_NUMBER):
        if i % 10000 == 0:
            print(f'{i} simulation run...')
        # get new birthdays list and append its dates to result
        birthdays = generate_date_list(get_random, int(birthdays_number))
        for x in birthdays:
            if x in results:
                results[x] += 1

    print(f'{SIMULATION_NUMBER} simulation run...')
    print(results)


"""generate a random list of {birthdays_number} birthdays as strings 'MthNN'"""

if __name__ == '__main__':
    main()