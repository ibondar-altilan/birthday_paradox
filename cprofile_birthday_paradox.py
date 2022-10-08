import cProfile
import pstats
from pstats import SortKey
import birthday_paradox
# import os


RUN_SCRIPT = 'yes'
# RUN_SCRIPT = 'no'

# get a script name from parent folder
# path = os.getcwd()
# parent = os.path.dirname(path)
# script_name = parent + '\\' + 'birthday_paradox.main()'

if RUN_SCRIPT == 'yes':
    cProfile.run('birthday_paradox.main()', 'bp_stats.log')  # run a script and save output to bp_stats.log


profile = pstats.Stats('bp_stats.log')
profile.sort_stats(SortKey.TIME)
profile.print_stats()

# profiling of initial version, first six snippets for an optimization
"""ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  2300023   20.217    0.000   20.886    0.000 birthday_paradox.py:19(get_string_date)
        2    5.170    2.585    5.170    2.585 {built-in method builtins.input}
  2300023    3.369    0.000    6.988    0.000 random.py:292(randrange)
   100001    2.566    0.000   30.801    0.000 birthday_paradox.py:27(generate_date_list)
  2300023    2.011    0.000    2.859    0.000 random.py:239(_randbelow_with_getrandbits)
  2300023    1.255    0.000    1.255    0.000 {method 'count' of 'list' objects}
"""
# optimization of get_string_date()






