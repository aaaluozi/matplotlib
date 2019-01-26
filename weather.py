import csv
from matplotlib import pyplot as plt
from datetime import datetime


def openfile(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        dates, highs, lows = get_date(reader)

    # header_row = next(reader)
    return dates, highs, lows


def get_date(reader):
    dates = []
    highs, lows = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            continue
            # print('missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows



