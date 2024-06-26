import matplotlib.pyplot as plt

size = [0, 10, 100, 1000, 10000]
BubbleTime = [0, 5.8, 344.2, 6264.4, 173364.4]
SelectionTime = [0, 5.6, 349.4, 3969.3,60945.9]
InsertionTime = [0, 5.6, 106.9, 2364.7, 16333.9]

plt.plot(size, BubbleTime)
plt.plot(size, SelectionTime)
plt.plot(size, InsertionTime)
plt.legend(["Bubble Sort", "Selection Sort", "Insertion Sort"])
plt.xlabel("Size")
plt.ylabel("Time in microseconds")
plt.show()