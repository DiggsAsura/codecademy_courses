# 7_2_2-Deque.py

import csv

def process_csv_supplies():
    data = []
    with open('supplies_data.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            data.append(row)
    return data