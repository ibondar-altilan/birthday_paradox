import timeit
import datetime
import random
from collections import Counter
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def generate_date_list(length, days_in_year):
    """Return a date list with length as strings 'MthDD'"""
    result = []
    for i in range(length):
        ordinal_date = random.randrange(1, days_in_year)
        date = datetime.date.fromordinal(ordinal_date)  # object of the date type
        string_date = MONTHS[date.month - 1] + ' ' + str(date.day)
        result.append(string_date)
    return result


def check_match_birthdays(birthdays):
    "Return a dict {date, number) of matching birthdays in group list"
    count = Counter()
    for x in birthdays:
        count[x] += 1
    return {k: v for (k, v) in count.items() if v > 1}
    # return count

"""def check_match_birthdays(birthdays):
    "Return a dict {date, number) of matching birthdays in group list"
    matches = {}
    for x in birthdays:
        number = birthdays.count(x)
        if number > 1:    # some matching found
            matches[x] = number
    return matches
"""


def main():
    setup = """\
from timing_birthday_paradox import check_match_birthdays
from timing_birthday_paradox import generate_date_list
birthdays = generate_date_list(23, 365)
"""
    code = 'check_match_birthdays(birthdays)'

    # setup = """from timing_birthday_paradox import generate_date_list; from random import randrange"""
    # code = 'generate_date_list(23, 365)'

    # setup = """from random import randrange"""
    # code = 'randrange(1, 365)'

    # setup = """from datetime import date; date = date.fromordinal(1)"""
    # code = """month = date.month"""

    # setup = 'result = []'
    # code = "result.append('Dec 31')"

    # setup = 'from timing_birthday_paradox import get_string_date'
    # code = 'get_string_date(365)'

    # setup = """from random import choice"""
    # code = 'choice(range(1, 365))'

    res = timeit.repeat(stmt=code, setup=setup, repeat=5, number=100_000)
    print(res)


if __name__ == '__main__':
    main()
