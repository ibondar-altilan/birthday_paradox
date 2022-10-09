import sys

from birthday_paradox import DAYS_IN_YEAR
from birthday_paradox import generate_date_list

# PYTHON_VERSION = (3, 9)                 # set a version manually
PYTHON_VERSION = sys.version_info     # get a current version


class TestGenerateDataList:
    length = 23
    days_in_year = DAYS_IN_YEAR
    result = generate_date_list(length, days_in_year)

    def test_list_length(self):
        assert len(self.result) == self.length

    def test_list_element_type(self):
        assert type(self.result[0]) == str

    def test_if_month(self):
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for x in self.result:
            assert x[:3] in self.months

    def test_if_day(self):
        # For Python < 3.10
        if PYTHON_VERSION < (3, 10):
            print()
            print('For versions < 3.10')
            for x in self.result:
                assert int(x[3:]) in range(1, 32)
        else:
            # for Python 3.10 with match construction
            print()
            print('For versions => 3.10')
            for x in self.result:
                match x[:3]:
                    case 'Jan' | 'Mar' | 'May' | 'Jul' | 'Aug' | 'Oct' | 'Dec':
                        assert int(x[3:]) in range(1, 32)
                    case 'Apr' | 'Jun' | 'Sep' | 'Nov':
                        assert int(x[3:]) in range(1, 31)
                    case 'Feb':
                        self.feb_days = 29
                        if DAYS_IN_YEAR == 365:
                            self.feb_days = 28
                        assert int(x[3:]) in range(1, self.feb_days + 1)
                    case _:
                        assert False, 'Incorrect month'
