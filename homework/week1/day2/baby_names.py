# -*- coding: utf-8 -*-
"""
In this example we are going to build an application that reads the most popular names
in the US, taken from the Social Security Administration's site:

https://www.ssa.gov/oact/babynames/

This application will have the following functionalities:

- It will accept a name as an argument
- It will read a list of files (located in the folder data). Each file contains the
most popular baby names for boys and girls for a certain year (the year is in the filename)
- For the name provided as an argument, print out how many years it's been among the most popular among boys and girls
"""

import numpy as np

def years(name):
    range_of_files = np.array(range(118)) + 1900
    count = 0
    for year in range_of_files:
        file = open('names_' + str(year) + '.txt', 'r')
        wholelist = file.read()
        lines = wholelist.split('\n')
        topline = lines[0].split('|')
        if name == topline[1] or name == topline[2]:
            count += 1
    print(count)

#%%
years('John')
years('Mary')
years('James')
years('Michael')
years('Jessica')
years('Brian')
