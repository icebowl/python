#!/usr/bin/env python3
# Random integers save file as rand-int.py
# generate random integer values
from random import seed
from random import randint
seed(110)
# generate some integers
for _ in range(10):
	value = randint(-100, 100)
	print(value," ",end="")
