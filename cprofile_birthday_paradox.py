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

# all profiles calculated for 23 birthdays
# profiling of initial version, first six snippets for an optimization
"""ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  2300023   20.217    0.000   20.886    0.000 birthday_paradox.py:19(get_string_date)
        2    5.170    2.585    5.170    2.585 {built-in method builtins.input}
  2300023    3.369    0.000    6.988    0.000 random.py:292(randrange)
   100001    2.566    0.000   30.801    0.000 birthday_paradox.py:27(generate_date_list)
  2300023    2.011    0.000    2.859    0.000 random.py:239(_randbelow_with_getrandbits)
  2300023    1.255    0.000    1.255    0.000 {method 'count' of 'list' objects}
"""
# optimizing of get_string_date(), in 10 times better: from 20.217 sec reduced to 2.076 sec (see a commit)
"""ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    5.197    2.599    5.197    2.599 {built-in method builtins.input}  # an input timing does not mean
  2300023    3.150    0.000    6.594    0.000 random.py:292(randrange)
   100001    2.076    0.000   11.576    0.000 birthday_paradox.py:28(generate_date_list)
  2300023    2.025    0.000    2.583    0.000 birthday_paradox.py:20(get_string_date)
  2300023    1.880    0.000    2.681    0.000 random.py:239(_randbelow_with_getrandbits)
  2300023    1.285    0.000    1.285    0.000 {method 'count' of 'list' objects}
  6900069    0.764    0.000    0.764    0.000 {built-in method _operator.index}
"""
# optimizing of generate_date_list(), app. 1 sec, deleting of get_string_date()
"""   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    5.116    2.558    5.117    2.558 {built-in method builtins.input}
   100001    3.269    0.000   10.692    0.000 birthday_paradox.py:20(generate_date_list)
  2300023    3.159    0.000    6.539    0.000 random.py:292(randrange)
  2300023    1.851    0.000    2.626    0.000 random.py:239(_randbelow_with_getrandbits)
  2300023    1.315    0.000    1.315    0.000 {method 'count' of 'list' objects}
  6900069    0.754    0.000    0.754    0.000 {built-in method _operator.index}
   100001    0.612    0.000    1.928    0.000 birthday_paradox.py:31(check_match_birthdays)
  2300023    0.552    0.000    0.552    0.000 {built-in method fromordinal}
"""
