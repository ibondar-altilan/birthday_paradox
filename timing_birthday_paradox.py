import timeit
import datetime
from datetime import date
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def get_string_date(date_as_ordinal):
    """Return string date 'Mth DD' or 'Mth D' from ordinal date"""
    date = datetime.date.fromordinal(date_as_ordinal)  # object of the date type
    # month = f'{date:%b}'  # fetch a month as 'Mth'
    # day = f'{date:%d}'  # fetch a date as 'NN'
    return MONTHS[date.month - 1] + ' ' + str(date.day)

def main():
    print(get_string_date(365))
    setup = 'from timing_birthday_paradox import get_string_date'
    code = 'get_string_date(1)'
    # setup = """from datetime import date; date = date.fromordinal(1)"""
    # code = """month = date.month"""
    res = timeit.timeit(stmt=code, setup=setup, number=230_000)
    print(res)


if __name__ == '__main__':
    main()
