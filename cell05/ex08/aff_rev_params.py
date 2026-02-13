#!/usr/bin/env python3

import sys

count = len(sys.argv) - 1

if count < 2:
    print("none")
else:
    for param in sys.argv[1:][::-1]:
        print(param)