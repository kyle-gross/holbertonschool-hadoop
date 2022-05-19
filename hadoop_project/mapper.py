#!/usr/bin/env python3
"""This module maps the rows of salaries.csv and prints them to stdout"""

import sys


cols = [
    'id', 'company', 'title', 'totalyearlycompensation',
    'location', 'yearsofexperience', 'yearsatcompany',
    'basesalary', 'stockgrantvalue', 'bonus'
]

for line in sys.stdin:
    line = line.strip()
    row = dict(zip(cols, [i.strip() for i in line.split(',')]))
    try:
        id = row['id']
        company = row['company']
        total_yearly = row['totalyearlycompensation']
        print(f'{id}\t{company},{total_yearly}')
    except:
        continue
