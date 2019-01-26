from matplotlib import pyplot as plt
from weather import openfile

filename1 = 'death_valley_2014.csv'
filename2 = 'sitka_weather_2014.csv'

dates_1, highs_1, lows_1 = openfile(filename1)
dates_2, highs_2, lows_2 = openfile(filename2)
#highs_1, lows_1 = get_tep(filename1)
# print(dates_1)
#print(highs_1)

# dates_2 = get_date(filename2)
# highs_2, lows_2 = get_tep(filename2)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_1, highs_1, c='red', alpha=0.5)
plt.plot(dates_1, lows_1, c='red', alpha=0.5)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='red', alpha=0.1)
plt.plot(dates_2, highs_2, c='blue', alpha=0.5)
plt.plot(dates_2, lows_2, c='blue', alpha=0.5)
plt.fill_between(dates_2, highs_2, lows_2, facecolor='blue', alpha=0.1)
# 设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
