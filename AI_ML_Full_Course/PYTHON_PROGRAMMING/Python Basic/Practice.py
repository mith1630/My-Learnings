#!/bin/python3

import math
import os
import random
import re
import sys


n = int(input().strip())
if n%2==0 and n==range(2,6):
    print("Not Weird")
        
elif n%2==0 and n==range(6,21):
    print("Weird")
        
elif n%2==0 and n > 20:
    print("Not Weird")
        
else:
    print("Weird")
