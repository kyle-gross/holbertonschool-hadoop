#!/usr/bin/env python3
"""This script serves as the reducer for the MapReduce function"""
import sys


cols = ['id', 'company', 'Salary']
top_10 = []

for line in sys.stdin:
    line = line.strip()
    row = dict(zip(cols,[i for i in line.replace('\t', ',').split(',')]))
    try:
        salary = float(row['Salary'])
        if len(top_10) < 10:
            top_10.append(row)
        else:
            for i in range(10):
                if salary > float(top_10[i]['Salary']):
                    top_10[i] = row
                    break
    except:
        continue

top_10 = reversed(sorted(top_10, key=lambda d: float(d['Salary'])))

print('id\tSalary\tcompany')
for row in top_10:
    id = row['id']
    salary = float(row['Salary'])
    company = row['company']
    print(f'{id}\t{salary}\t{company}')
