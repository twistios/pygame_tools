import matplotlib.pyplot as plt

# line 1 points
x1 = [1,2,3,4,5]
# y1 = [750.588,747.595,736.189,757.119,728.285] # 1.9.6
y1 = [820.757,811.532,825.576,810.174,809.225] # 2.0
# plotting the line 1 points
plt.plot(x1, y1, label = "no blit")

# line 2 points
x2 = [1,2,3,4,5]
# y2 = [719.135,727.915,723.636,718.309,722.236] # 1.9.6
y2 = [745.560,758.214,761.649,755.435,746.319] # 2.0
# plotting the line 2 points
plt.plot(x2, y2, label = "simple blit")

# line 3 points
x3 = [1,2,3,4,5]
# y3 = [724.047,741.564,715.580,718.817,715.476] # 1.9.6
y3 = [767.275,733.861,727.157,758.929,755.865] # 2.0
# plotting the line 3 points
plt.plot(x3, y3, label = "simple shape")

# naming the x axis
plt.xlabel('test run')
# naming the y axis
plt.ylabel('updates/s')
# giving a title to my graph
# plt.title('Pygame 1.9.6 Benchmark')
plt.title('Pygame 2.0.0 Benchmark')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
