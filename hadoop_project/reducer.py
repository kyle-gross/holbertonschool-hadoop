#!/usr/bin/env python3
"""This script serves as the reducer for the MapReduce function"""

import sys
from datetime import datetime

cols = ['id', 'company', 'Salary']
top_10 = []

now = datetime.now()
for line in sys.stdin:
    line = line.strip()
    row = dict(zip(cols, [i for i in line.replace('\t', ',').split(',')]))
    try:
        salary = float(row['Salary'])
        top_10.append(row)
    except:
        continue

top_10 = list(reversed(sorted(top_10, key=lambda d: float(d['Salary']))))[:10]

print('id\tSalary\tcompany')
for row in top_10:
    id = row['id']
    salary = float(row['Salary'])
    company = row['company']
    print(f'{id}\t{salary}\t{company}')
