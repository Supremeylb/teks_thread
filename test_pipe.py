"""
Find the sum of multiples of 3 or 5 below 1000
[description]
""" 
from pipe import *
import itertools
(itertools.count() | select(lambda x: x * 3) | take_while(lambda x: x < 1000) | add) \
       + (itertools.count() | select(lambda x: x * 5) | take_while(lambda x: x < 1000) | add) \
       - (itertools.count() | select(lambda x: x * 15) | take_while(lambda x: x < 1000) | add) | stdout

"""
square = lambda x:x * x
(itertools.count(1) | take(100) | select(square) | add)
[description]
"""