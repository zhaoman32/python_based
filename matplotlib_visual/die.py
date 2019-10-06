from random import randint
# 模拟掷骰子
import pygal


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

# -------------------------------------------


die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = range(2,11)
hist._x_title = 'Results'
hist.y_title = "Frequency of Result"

hist.add("D6 + D6", frequencies)
hist.render_to_file('die_visual.svg')
