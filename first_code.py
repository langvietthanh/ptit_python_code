# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import groupby
import math
import os
import random
import re
import sys
from collections import Counter,defaultdict,deque,namedtuple,OrderedDict

n = int (input())
lst = list(map(int,input().split()))
for item in lst:
    print (item)