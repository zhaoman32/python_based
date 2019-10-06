import csv
from datetime import datetime
# datetime.strptime("2014-7-2", "%Y-%m-%d")将字符串处理成标准时间

import matplotlib.pyplot as plt

filename = "sitka_weather_2018.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column in enumerate(header_row):
        print(index, column)
        # 发现2 DATE, 7 TAVG, # 8 TMAX, # 9 TMIN
    dates, highs, lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[8])
            low = int(row[9])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # 区域着色
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title("Daily high and low temperatures", fontsize=24)
    plt.xlabel("", fontsize=16)
    # 倾斜日期标签
    fig.autofmt_xdate()
    plt.ylabel("Temperatures", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()