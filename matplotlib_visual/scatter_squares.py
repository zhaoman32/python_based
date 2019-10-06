import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

# plt.scatter(x_value, y_value, c=(0, 0, 0.8), edgecolors='none', s=40)
# 颜色的渐变映射
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.title("Squares number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 注意将show替换成savefig
plt.savefig("squares_plot.png", bbox_inches='tight')