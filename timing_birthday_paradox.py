import timeit
import datetime
import random
from datetime import date
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def get_string_date(date_as_ordinal):
    """Return string date 'Mth DD' or 'Mth D' from ordinal date"""
    date = datetime.date.fromordinal(date_as_ordinal)  # object of the date type
    return MONTHS[date.month - 1] + ' ' + str(date.day)


# def generate_date_list(length, days_in_year):
#     """Return a date list with length as strings 'MthDD'"""
#     result = []
#     for i in range(length):
#         ordinal_date = random.randrange(1, days_in_year)
#         string_date = get_string_date(ordinal_date)
#         result.append(string_date)
#     return result

def generate_date_list(length, days_in_year):
    """Return a date list with length as strings 'MthDD'"""
    result = []
    for i in range(length):
        ordinal_date = random.randrange(1, days_in_year)
        date = datetime.date.fromordinal(ordinal_date)  # object of the date type
        string_date = MONTHS[date.month - 1] + ' ' + str(date.day)
        result.append(string_date)
    return result


def main():
    print(get_string_date(365))
    setup = """from timing_birthday_paradox import generate_date_list; from random import randrange"""
    code = 'generate_date_list(23, 365)'

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

    res = timeit.timeit(stmt=code, setup=setup, number=100_000)
    print(res)


if __name__ == '__main__':
    main()
